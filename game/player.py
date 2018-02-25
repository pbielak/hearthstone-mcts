"""Player module"""


class Player(object):
    """
    Health
    Mana points

    Cards
    Minions
    """
    def __init__(self, name, cfg):
        self.name = name
        self.health = cfg.INITIAL_HEALTH
        self.mana = cfg.INITIAL_MANA
        self.cards = []
        self.minions = []
        self.cfg = cfg

    def __repr__(self):
        fmt_str = "Player: {name}; Health: {current_health}/{max_health}; " \
                  "Mana: {current_mana}/{max_mana}; " \
                  "Cards: {cards}; " \
                  "Minions: {minions}"

        return fmt_str.format(name=self.name,
                              current_healt=self.health,
                              max_health=self.cfg.INITIAL_HEALTH,
                              current_mana=self.mana,
                              max_mana=self.cfg.INITIAL_MANA,
                              cards=self.cards,
                              minions=self.minions)
