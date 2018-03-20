"""MCTS Tree Node"""
from collections import Counter
from copy import deepcopy
import math

import numpy as np

from game import action
from mcts.turn import TurnGenerator


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

    def is_terminal(self):
        pass

    def is_fully_expanded(self):
        pass

    def expand(self):
        pass

    def get_best_child(self, coeff):
        pass

    def __repr__(self):
        return "{}(id={}, children={}, visited={}, reward={})".format(
            self.__class__.__name__,
            self.id,
            [child.id if child else "None" for child in self.children],
            self.visited,
            self.reward
        )


class DecisionTurnNode(Node):
    def __init__(self, state, parent, turns):
        #print('Creating DecisionTurnNode!')
        super(DecisionTurnNode, self).__init__(state, parent)

        self.turns = turns

    def is_terminal(self):
        return (not self.turns and not self.children) or self.state.is_terminal_state()  # not self.children

    def is_fully_expanded(self):
        return not self.turns

    def expand(self):
        chosen_turn = self.turns.pop()

        new_child = DrawCardNode(state=chosen_turn.game_state,
                                 parent=self,
                                 turn=chosen_turn)
        self.children.append(new_child)
        return new_child.expand()

    def get_best_child(self, coeff):
        best_child = None
        best_child_score = -99999

        for child in self.children:
            score = child.reward / child.visited + \
                    coeff * math.sqrt(2 * math.log(self.visited)/child.visited)

            if score > best_child_score:
                best_child_score = score
                best_child = child

        return best_child


class DrawCardNode(Node):
    def __init__(self, state, parent, turn):
        #print('Creating DrawCardNode!')
        super(DrawCardNode, self).__init__(state, parent)

        self.turn = turn

        self.possible_cards = None
        self.probs = None
        self.children = None

        self._get_all_card_draws(state)

    def is_terminal(self):
        return False

    def is_fully_expanded(self):
        return self.children.count(None) == 0

    def expand(self, idx=None):
        if idx is None:
            not_expanded_idx = -1
            for idx, elem in enumerate(self.children):
                if elem is None:
                    not_expanded_idx = idx
                    break

            assert not_expanded_idx != -1
        else:
            not_expanded_idx = idx

        self.children[not_expanded_idx] = self._create_child(not_expanded_idx)

        if isinstance(self.children[not_expanded_idx], DrawCardNode):
            return self.children[not_expanded_idx].expand()

        return self.children[not_expanded_idx]

    def get_best_child(self, coeff):
        selected_card_idx = np.random.choice(
            len(self.possible_cards),
            p=self.probs
        )

        if self.children[selected_card_idx] is None:
            self.expand(selected_card_idx)

        return self.children[selected_card_idx]

    def _get_all_card_draws(self, game_state):
        player, _ = game_state.get_players()

        if player.deck.is_empty():
            # If deck is empty, there is only one possible child,
            # which is created by reducing the players health
            self.possible_cards = [None]
            self.probs = [1.0]

            game_state_cpy = deepcopy(game_state)
            player, _ = game_state_cpy.get_players()
            player.deck.no_attempt_pop_when_empty += 1
            player.health -= player.deck.no_attempt_pop_when_empty

            self.children = [DecisionTurnNode(state=game_state_cpy,
                                              parent=self)]
            return

        nb_cards_in_deck = len(player.deck.cards)
        possible_cards = []
        probabilities = []

        for card, nb_card in Counter(player.deck.cards).items():
            possible_cards.append(card)
            probabilities.append(nb_card / nb_cards_in_deck)

        self.possible_cards = possible_cards
        self.probs = probabilities
        self.children = [None] * len(self.possible_cards)

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

        # Check if any turns are possible
        turns = TurnGenerator().generate_all_turns(game_state_cpy)
        if not turns:
            game_state_cpy.curr_step += 1
            player, _ = game_state_cpy.get_players()
            action.increment_mana(player)
            player.already_used_mana = 0
            return DrawCardNode(state=game_state_cpy, parent=self, turn=None)

        return DecisionTurnNode(state=game_state_cpy, parent=self, turns=turns)
