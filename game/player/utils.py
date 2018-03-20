"""Utils"""
from copy import deepcopy

from game import action
from game import config
from game.cards import card as cards
from game.cards import deck


def can_use_card(player, card):
    return player.already_used_mana + card.cost <= player.mana


def can_put_minion(player):
    return len(player.minions) < config.MAX_MINIONS


def cleanup_all_dead_minions(game_state):
    for player in (game_state.player_A, game_state.player_B):
        player.minions = [
            minion for minion in player.minions if minion.health > 0
        ]


def get_possible_actions(game_state):
    actions = {
        'spell_plays': [],
        'minion_puts': [],
        'minion_plays': [],
        'no_actions': None
    }

    player, opponent = game_state.get_players()

    for idx, card in enumerate(player.cards):
        if not can_use_card(player, card):
            continue

        # Play spell cards
        if isinstance(card, cards.SpellCard):
            actions['spell_plays'].append(
                (action.play_spell, (idx, game_state))
            )
        # Put minion cards
        elif isinstance(card, cards.MinionCard):
            if not can_put_minion(player):
                continue
            actions['minion_puts'].append(
                (action.put_minion, (idx, game_state))
            )

    # Play minion (attack)
    for idx, minion in enumerate(player.minions):
        if not minion.can_attack:
            continue

        for target_idx in (-1, *list(range(len(opponent.minions)))):
            actions['minion_plays'].append(
                (action.play_minion, (idx, target_idx, game_state))
            )

    actions['no_actions'] = (not actions['spell_plays']) and \
                            (not actions['minion_plays']) and \
                            (not actions['minion_puts'])

    return actions


def create_player_from_default_config(player_cls, name):
    return player_cls(name=name,
                      health=config.INITIAL_HEALTH,
                      mana=config.INITIAL_MANA,
                      already_used_mana=0,
                      deck=deck.CardDeck(),
                      cards=list(),
                      minions=list())


def create_player_from_another_player(target_player_cls, source_player_obj):
    return target_player_cls(name=source_player_obj.name,
                             health=source_player_obj.health,
                             mana=source_player_obj.mana,
                             already_used_mana=source_player_obj.already_used_mana,
                             deck=deepcopy(source_player_obj.deck),
                             cards=deepcopy(source_player_obj.cards),
                             minions=deepcopy(source_player_obj.minions))
