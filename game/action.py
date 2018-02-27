"""Player action"""


class Action(object):
    """
    Single action like:
        * take card from deck (always forced; if no cards in deck,
                               loose health points)
        * play minion card (attack; against whom?)
        * play curse / magic card
        * put minion on field (max. 7 on field)
    """
    pass

# Action:
# * Draw card: (GameState, Player) -> GameState
# * Play spell: (GameState,



# GUI
#       Player B Name (Health: xx/20)
# Cards: [XYZ ABC QWE]
# Minions: [ SuperMinion1 SuperMinion2 ]
# ---------------------------------------
# Minions: [ SuperMinion3 ]
# Cards: [NMB HJK IOP]
#       Player A Name (Health: yy/20)
# ======================================
# Which action?
# 0. Take card
# 1. Put minion on field (which one?)
# 2. Call spell card (which one?)
# 3. Attack with minion (which one? whom?)

class Turn(object):
    """
    list(Action)
    """
    pass
