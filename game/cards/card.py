"""Base Card class"""
from copy import deepcopy


class Card(object):
    """Base class for all cards
    """

    def apply(self, game_state, source, target):
        """
        This method should be implemented in all classes, which inherit from
        this class. It should take the current game state, perform a deepcopy,
        modify the copy (according to the effect of the actual card) and return
        the modified game state.

        :param game_state: current game state, should NOT be modified directly
        :param source: the player which called this card
        :param target: the targeted player or enemy minion (if a card does not
                       need a target - like updating the stats of the current
                       player, then assume that "target = None")
        :return: modified copy of input game state
        """
        pass


class SpellCard(Card):
    """Card representing a spell.

    Attributes:
        * name (str): name of card
        * cost (int): number of mana points necessary to use this card
        * effect (func: (GameState, Player, Player/Minion) -> GameState):
                effect of the card
    """
    def __init__(self, name, cost, effect):
        self.name = name
        self.cost = cost
        self.effect = effect

    def apply(self, game_state, source, target):
        return self.effect(game_state, source, target)

    def __repr__(self):
        fmt_str = "SpellCard: {name}; " \
                  "Cost: {cost}; " \
                  "Effect: {effect}"

        return fmt_str.format(name=self.name,
                              cost=self.cost,
                              effect=self.effect)


class MinionCard(Card):
    """Card representing a minion.

    Attributes:
        * name (str): name of card
        * health (int): number of health points
        * attack (int): number of health points
        * cost (int): number of mana points necessary to use this card
        * side-effect (func: (GameState, Player, Player/Minion) -> GameState):
            optional side effect
    """
    def __init__(self, name, health, attack, cost, side_effect=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.cost = cost
        self.side_effect = side_effect

    def apply(self, game_state, source, target):
        # Call side-effect
        if self.side_effect is not None:
            game_state_cpy = self.side_effect(game_state, source, target)
        else:
            game_state_cpy = deepcopy(game_state)

        # Perform attack
        if target is game_state.player_A:
            game_state_cpy.player_A.health -= self.attack
        elif target is game_state.player_B:
            game_state_cpy.player_B.health -= self.attack
        elif isinstance(target, MinionCard):
            for idx, minion in enumerate(game_state.player_A.minions):
                if target is minion:
                    game_state_cpy.player_A.minions[idx].health -= self.attack
            for idx, minion in enumerate(game_state.player_B.minions):
                if target is minion:
                    game_state_cpy.player_B.minions[idx].health -= self.attack
        else:
            raise ValueError('Target not defined or not recognized!')

        return game_state_cpy

    def __repr__(self):
        fmt_str = "MinionCard: {name}; " \
                  "Health: {health}; " \
                  "Attack: {attack}; " \
                  "Cost: {cost}; " \
                  "Side-effect: {side_effect}"

        return fmt_str.format(name=self.name, health=self.health,
                              attack=self.attack, cost=self.cost,
                              side_effect=self.side_effect)

