"""Hearthstone game state"""
from game.cards.deck import CardDeck


class GameState(object):
    """
    Player A <--- CardDeck A
    Player B <--- CardDeck B
    """
    def __init__(self, cfg):
        self.player_A = cfg.player_A_cls('Pyjter', cfg)
        self.card_deck_A = CardDeck(self.player_A.name)

        self.player_B = cfg.player_B_cls('Mati', cfg)
        self.card_deck_B = CardDeck(self.player_B.name)

    def is_terminal_state(self):
        """Check if game is over (one player lost)"""
        is_player_A_dead = self.player_A.health <= 0
        is_player_B_dead = self.player_B.health <= 0
        return is_player_A_dead or is_player_B_dead

    def __repr__(self):
        fmt_str = "GameState: Player A: {player_A}; \n" \
                  "Deck A: {deck_A}; \n" \
                  "Player B: {player_B}; \n" \
                  "Deck B: {deck_B};\n"

        return fmt_str.format(player_A=self.player_A,
                              deck_A=self.card_deck_A,
                              player_B=self.player_B,
                              deck_B=self.card_deck_B)
