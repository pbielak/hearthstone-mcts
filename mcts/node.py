"""MCTS Tree Node"""
from collections import Counter
from copy import deepcopy

import numpy as np


class Node(object):
    NODE_ID_COUNTER = 0

    def __init__(self, state, parent):
        self.id = Node.NODE_ID_COUNTER
        Node.NODE_ID_COUNTER += 1

        self.state = state
        self.parent = parent
        self.children = []

        self.visited = 0
        self.reward = 0

    def __repr__(self):
        return "{}(id={}, children={})".format(
            self.__class__.__name__,
            self.id,
            [child.id if child else "None" for child in self.children]
        )


class DecisionTurnNode(Node):
    def __init__(self, state, parent):
        super(DecisionTurnNode, self).__init__(state, parent)

        self.actions = []
        self.action = None

    def is_leaf(self):
        return not self.children

    def is_fully_expanded(self):
        return not self.actions

    def __repr__(self):
        fmt_str = "Node(" \
                  "S: {state}," \
                  "P: {parent}," \
                  "C: {children})"

        return fmt_str.format(state=self.state,
                              parent=self.parent,
                              children=self.children)


class DrawCardNode(Node):
    def __init__(self, state, parent):
        super(DrawCardNode, self).__init__(state, parent)

        self.possible_cards, self.probs = self._get_all_card_draws(state)
        self.children = [None] * len(self.possible_cards)

    def choose_child(self):
        selected_card_idx = np.random.choice(
            len(self.possible_cards),
            p=self.probs
        )

        print(selected_card_idx)

        if self.children[selected_card_idx] is None:
            # First time this child is selected,
            # so it needs to be created
            self.children[selected_card_idx] = self._create_child(
                                                        selected_card_idx)
        return self.children[selected_card_idx]

    @staticmethod
    def _get_all_card_draws(game_state):
        player, _ = game_state.get_players()

        nb_cards_in_deck = len(player.deck.cards)
        possible_cards = []
        probabilities = []

        for card, nb_card in Counter(player.deck.cards).items():
            possible_cards.append(card)
            probabilities.append(nb_card / nb_cards_in_deck)

        return possible_cards, probabilities

    def _create_child(self, card_idx):
        game_state_cpy = deepcopy(self.state)
        card_name = self.possible_cards[card_idx].name

        # Get card from deck
        player, _ = game_state_cpy.get_players()
        card = None

        for c in player.deck.cards:
            if c.name == card_name:
                card = c
                break

        assert card is not None

        # Put into cards (hand)
        player.cards.append(card)

        # Remove from deck
        player.deck.cards.remove(card)

        return DecisionTurnNode(state=game_state_cpy, parent=self)
