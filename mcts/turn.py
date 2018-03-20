"""
Turn generation for MCTS player
"""
from copy import deepcopy
import time

from game.player import utils as pl_utils


class Turn(object):
    def __init__(self):
        self.actions = []
        self.game_state = None
        self.is_terminal = False

    def __repr__(self):
        if self.is_terminal:
            return "TurnTERMINAL(actions={})".format(self.actions)
        return "Turn(actions={})".format(self.actions)


class TurnGenerator(object):
    def __init__(self, max_calculation_time=5):
        self.max_calculation_time = max_calculation_time  # in seconds
        self.start_time = 0
        self.current_time = 0

    def _time_limit_exceeded(self):
        return self.current_time - self.start_time > self.max_calculation_time

    def generate_all_turns(self, game_state):
        """
        Generate all possible turns
        :param game_state: MUST BE A COPY OF THE CURRENT GAME_STATE (!)
        :return: list of Turn objects
        """
        self.start_time = time.time()

        # Generate initial expansion of possible actions
        turns = list()

        initial_turns = self._create_initial_turns(game_state)
        if not initial_turns:
            return []

        turns.append(initial_turns)
        self.current_time = time.time()

        while not self._time_limit_exceeded():
            nth_level_turns = self._create_nth_level_turns(turns[-1])
            if not nth_level_turns:
                break

            turns.append(nth_level_turns)
            self.current_time = time.time()

        print(
            'Turn generation took:',
            round(self.current_time - self.start_time, 5),
            ' (s)'
        )

        turns_flattened = [t for lvl_turn in turns for t in lvl_turn]
        return turns_flattened

    def _create_initial_turns(self, game_state):
        turns = []
        for pa in self._get_list_of_possible_actions(game_state):
            turn = Turn()
            turn.actions.append(pa)
            turn.game_state = self._transform(game_state, pa)
            turns.append(turn)

            # If there is no time left...
            self.current_time = time.time()
            if self._time_limit_exceeded():
                return turns

        return turns

    def _create_nth_level_turns(self,  prev_lvl_turns):
        nth_lvl_turns = []

        for turn in prev_lvl_turns:
            if turn.is_terminal:
                continue

            for pa in self._get_list_of_possible_actions(turn.game_state):
                turn_cpy = deepcopy(turn)
                turn_cpy.actions.append(pa)

                turn_cpy.game_state = self._transform(turn.game_state, pa)
                # Perform game_state consistency checks
                pl_utils.cleanup_all_dead_minions(turn_cpy.game_state)
                if turn_cpy.game_state.is_terminal_state():
                    turn_cpy.is_terminal = True

                nth_lvl_turns.append(turn_cpy)

                # If there is no time left...
                self.current_time = time.time()
                if self._time_limit_exceeded():
                    return nth_lvl_turns

        return nth_lvl_turns

    @staticmethod
    def _get_list_of_possible_actions(game_state):
        pas = pl_utils.get_possible_actions(game_state)
        return [*pas['spell_plays'], *pas['minion_plays'], *pas['minion_puts']]

    @staticmethod
    def _transform(curr_game_state, action):
        game_state_cpy = deepcopy(curr_game_state)

        action_func, args = action
        # Replace applied game_state with current copy
        new_args = args[:-1] + (game_state_cpy,)

        action_func(*new_args)
        return game_state_cpy
