import random

from hashlib import md5

TRACE_SOL = 'tests/play.sol'
TEST_SEED = 1337
NUM_TESTS = 1000

def hash(val):
    return int(md5(str(val).encode()).hexdigest(), base=16) & 0xffffffff

def make_random_strat():
    """Makes a random pure strategy."""
    seed = random.randrange(0, 2 ** 31)

    def random_strat(score, opponent_score):
        # Save the state of the random generator, so strategy calls don't
        # impact dice rolls.
        state = random.getstate()
        random.seed(hash((score, opponent_score, seed)))
        roll = random.randrange(0, 11)
        random.setstate(state)
        return roll
    return random_strat


class GameTurn(object):
    def __init__(self, score, opponent_score, who, num_rolls):
        if who == 0:
            self.score0, self.score1 = score, opponent_score
        else:
            self.score0, self.score1 = opponent_score, score
        self.who = who
        self.num_rolls = num_rolls
        self.rolls = []
        self.dice_sides = 6
        self.score0_final, self.score1_final = None, None

    def is_over(self):
        """Returns True iff this GameTurn should be over."""
        return len(self.rolls) >= self.num_rolls

    def is_successor(self, other):
        """Returns True if another GameTurn is a plausible successor of this
        GameTurn. Used for preventing multiple calls to a strategy function
        from messing up the tracer (to a reasonable degree)."""
        # In case students call a strategy multiple times per turn.
        if self.who == other.who:
            return False
        # In case students call both strategies regardless of whose turn it is
        if self.score0 == other.score0 and self.score1 == other.score1 or \
                not self.is_over():
            return False
        # In case students call a strategy after the game should be over
        if max(other.score0, other.score1) >= 100:
            return False
        return True

    def set_successor(self, other):
        """Sets another GameTurn as the successor of this GameTurn."""
        self.score0_final , self.score1_final = other.score0, other.score1

    def is_correct(self, sol_hash):
        """Returns True if the hash of this GameTurn matches the solution
        hash."""
        return hash(self) == sol_hash

    @property
    def turn_summary(self):
        """Returns a string containing a description of how who rolled how many
        dice this turn."""
        if self.num_rolls == 0:
            return 'Player {0} rolls 0 dice:'.format(self.who)
        elif self.num_rolls == 1:
            return 'Player {0} rolls {1} {2}-sided die:'.format(
                    self.who,
                    self.num_rolls,
                    'six' if self.dice_sides == 6 else 'four')
        else:
            return 'Player {0} rolls {1} {2}-sided dice:'.format(
                    self.who,
                    self.num_rolls,
                    'six' if self.dice_sides == 6 else 'four')

    @property
    def turn_rolls(self):
        """Returns a string containing the dice values rolled this turn."""
        return str(self.rolls)[1:-1]

    @property
    def dice_summary(self):
        """Returns a string containing a summary of the dice values rolled this
        turn."""
        if len(self.rolls) == 0:
            return ''
        return 'Dice sum: {0} {1}'.format(
                sum(self.rolls),
                '(rolled ones)' if 1 in self.rolls else '')

    def __repr__(self):
        return str((self.score0, self.score1, self.score0_final,
                self.score1_final, self.who, self.num_rolls, self.dice_sides))


def make_traced(s0, s1, six_sided, four_sided):
    """Given the strategy functions of player 0 and player 1, and six-sided and
    four-sided dice, returns traced versions of the function to be used for the
    game, as well as a function to retrieve the trace.  """
    trace = []  # List of GameTurns

    def make_traced_strategy(strat, player):
        def traced_strategy(score, opponent_score):
            num_rolls = strat(score, opponent_score)
            state = GameTurn(score, opponent_score, player, num_rolls)

            if not trace:
                trace.append(state)
            elif trace[-1].is_successor(state):
                trace[-1].set_successor(state)
                trace.append(state)
            return num_rolls
        return traced_strategy

    def make_traced_dice(dice, dice_sides):
        def traced_dice():
            roll = dice()
            if trace:
                trace[-1].dice_sides = dice_sides
                trace[-1].rolls.append(roll)
            return roll
        return traced_dice

    def get_trace(score0, score1):
        """Given the final score outcome of the game, returns the trace of the
        game."""
        trace[-1].score0_final = score0
        trace[-1].score1_final = score1
        return trace

    return make_traced_strategy(s0, 0), \
        make_traced_strategy(s1, 1), \
        make_traced_dice(six_sided, 6), \
        make_traced_dice(four_sided, 4), \
        get_trace


def play_traced(hog, strat0, strat1):
    """Returns the trace of a hog game, given the HOG module, as well as the
    player 0 and 1 strategies for the game."""
    four_sided, six_sided = hog.four_sided, hog.six_sided
    strat0, strat1, traced_six_sided, traced_four_sided, get_trace = \
        make_traced(strat0, strat1, six_sided, four_sided)

    hog.four_sided = traced_four_sided
    hog.six_sided = traced_six_sided
    score0, score1 = hog.play(strat0, strat1)
    trace = get_trace(score0, score1)

    hog.four_sided = four_sided
    hog.six_sided = six_sided
    return trace


def check_play_function(hog):
    """Checks the `play` function of a student's HOG module by running multiple
    seeded games, and comparing the results."""
    random.seed(TEST_SEED)
    sol_traces = load_traces_from_file(TRACE_SOL)
    for i in range(NUM_TESTS):
        strat0, strat1 = make_random_strat(), make_random_strat()
        trace = play_traced(hog, strat0, strat1)
        incorrect = compare_trace(trace, sol_traces[i])
        if incorrect != -1:
            print('Incorrect result after playing {0} game(s):'.format(i + 1))
            print_trace(trace, incorrect)
            print('Incorrect implementation of game at turn {0}.'.format(incorrect))
            print('Please read over the trace to find your error.')
            print("\nIf you're having trouble, try looking up the error ID on Piazza,")
            print('or making a post with this full trace output.')
            print('(error_id: {0})'.format(
                hash((trace[incorrect], incorrect, i))))
            break


def make_solution_traces(hog):
    """Given a reference HOG solution module, returns the hashed solution
    trace."""
    random.seed(TEST_SEED)
    sol_traces = []
    for i in range(NUM_TESTS):
        strat0, strat1 = make_random_strat(), make_random_strat()
        trace = play_traced(hog, strat0, strat1)
        sol_traces.append([hash(state) for state in trace])
    return sol_traces


def compare_trace(trace, sol):
    """Compares TRACE with the SOLUTION trace, and returns the turn number
    where the two traces differ, or -1 if the traces are the same.
    """
    i = 0
    while i < min(len(trace), len(sol)):
        state, sol_state = trace[i], sol[i]
        if not state.is_correct(sol_state):
            return i
        i += 1
    if len(trace) != len(sol):
        return len(trace)
    return -1


def print_trace(trace, incorrect=None):
    """Prints out the student trace."""
    print('-'*64)
    print('{0:>10}{1:>8}{2:>8}    {3}'.format(
        '',
        'score0',
        'score1',
        'Turn Summary'))
    print('-'*64)
    for i, turn in enumerate(trace):
        if incorrect is not None and i != incorrect:
            continue
        s0_change = turn.score0_final - turn.score0
        s1_change = turn.score1_final - turn.score1
        print('{0:<10}{1:8}{2:8}    {3}'.format(
            'Turn {0}:'.format(i),
            turn.score0,
            turn.score1,
            turn.turn_summary))
        print('{0:<10}{1:>8}{2:>8}        {3}'.format(
            '',
            '' if s0_change == 0 else '{0:+}'.format(s0_change),
            '' if s1_change == 0 else '{0:+}'.format(s1_change),
            turn.turn_rolls))
        print('{0:<10}{1:8}{2:8}    {3}'.format(
            '',
            turn.score0_final,
            turn.score1_final,
            turn.dice_summary))
        print('-'*64)
    print('{0:<15}{1:3}{2:8}'.format(
        'Final Score:',
        turn.score0_final,
        turn.score1_final))
    print('-'*64)


def load_traces_from_file(path):
    """Given a file specified by a PATH, returns a trace."""
    with open(path) as f:
        return eval(f.read())

def write_traces_to_file(path, traces):
    """Given a target file specified by a PATH, and a solution trace, writes
    the trace to the file."""
    with open(path, 'w') as f:
        f.write(str(traces))
