# Q2
def if_this_not_that(i_list, this):
    """Define a function which takes a list of integers `i_list` and an integer
    `this`. For each element in `i_list`, print the element if it is larger
    than `this`; otherwise, print the word "that".

    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    "*** YOUR CODE HERE ***"
    for integer in i_list:
        if integer > this:
            print(integer)
        else:
            print("that")

# Q4
def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    return city[2]

from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    "*** YOUR CODE HERE ***"
    return sqrt((get_lat(city1) - get_lat(city2))**2+ (get_lon(city1) - get_lon(city2))**2)

# Q5
def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    temporary_city = make_city("temporary city", lat, lon)
    distance1 = distance(temporary_city, city1)
    distance2 = distance(temporary_city, city2)
    if distance1 > distance2:
        return get_name(city2)
    else:
        return get_name(city1)

# Connect N: Q6-11
######################
### Connect N Game ###
######################

def create_row(size):
    """Returns a single, empty row with the given size. Each empty spot is
    represented by the string '-'.

    >>> create_row(5)
    ['-', '-', '-', '-', '-']
    """
    "*** YOUR CODE HERE ***"
    return ['-' for i in range(size)]


def create_board(rows, columns):
    """Returns a board with the given dimensions.

    >>> create_board(3, 5)
    [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]
    """
    "*** YOUR CODE HERE ***"
    return [create_row(columns) for row in range(rows)]


def replace_elem(lst, index, elem):
    """Create and return a new list whose elements are the same as those in
    LST except at index INDEX, which should contain element ELEM instead.

    >>> old = [1, 2, 3, 4, 5, 6, 7]
    >>> new = replace_elem(old, 2, 8)
    >>> new
    [1, 2, 8, 4, 5, 6, 7]
    >>> new is old   # check that replace_elem outputs a new list
    False
    """
    assert index >= 0 and index < len(lst), 'Index is out of bounds'
    "*** YOUR CODE HERE ***"
    return lst[:index] + [elem] + lst[(index + 1):]


def get_piece(board, row, column):
    """Returns the piece at location (row, column) in the board.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> board = put_piece(board, rows, 0, 'X')[1] # Puts piece "X" in column 0 of board and updates board
    >>> board = put_piece(board, rows, 0, 'O')[1] # Puts piece "O" in column 0 of board and updates board
    >>> get_piece(board, 1, 0)
    'X'
    >>> get_piece(board, 1, 1)
    '-'
    """
    "*** YOUR CODE HERE ***"
    return board[row][column]


def put_piece(board, max_rows, column, player):
    """Puts PLAYER's piece in the bottommost empty spot in the given column of
    the board. Returns a tuple of two elements:

        1. The index of the row the piece ends up in, or -1 if the column
           is full.
        2. The new board

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, new_board = put_piece(board, rows, 0, 'X')
    >>> row
    1
    >>> row, new_board = put_piece(new_board, rows, 0, 'O')
    >>> row
    0
    >>> row, new_board = put_piece(new_board, rows, 0, 'X')
    >>> row
    -1
    """
    "*** YOUR CODE HERE ***"
    for row in range(max_rows - 1, -1, -1):
        if get_piece(board, row, column) == '-':
            new_row = replace_elem(board[row], column, player)  # Replace the item in the row
            new_board = replace_elem(board, row, new_row)  # Replace the row in the board
            return row, new_board
    return -1, board



def make_move(board, max_rows, max_cols, col, player):
    """Put player's piece in column COL of the board, if it is a valid move.
    Return a tuple of two values:

        1. If the move is valid, make_move returns the index of the row the
           piece is placed in. Otherwise, it returns -1.
        2. The updated board

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, board = make_move(board, rows, columns, 0, 'X')
    >>> row
    1
    >>> get_piece(board, 1, 0)
    'X'
    >>> row, board = make_move(board, rows, columns, 0, 'O')
    >>> row
    0
    >>> row, board = make_move(board, rows, columns, 0, 'X')
    >>> row
    -1
    >>> row, board = make_move(board, rows, columns, -4, '0')
    >>> row
    -1
    """
    "*** YOUR CODE HERE ***"
    if 0 <= col < max_cols:
        return put_piece(board, max_rows, col, player)
    else:
        return -1, board

def print_board(board, max_rows, max_cols):
    """Prints the board. Row 0 is at the top, and column 0 at the far left.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> print_board(board, rows, columns)
    - -
    - -
    >>> new_board = make_move(board, rows, columns, 0, 'X')[1]
    >>> print_board(new_board, rows, columns)
    - -
    X -
    """
    "*** YOUR CODE HERE ***"
    for row in range(max_rows):
        row_elem = ''
        for column in range(max_cols):
            row_elem = row_elem + get_piece(board, row, column) + ' '
        print(row_elem.strip())


def check_win_row(board, max_rows, max_cols, num_connect, row, player):
    """ Returns True if the given player has a horizontal win
    in the given row, and otherwise False.

    >>> rows, columns, num_connect = 4, 4, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'O')
    False
    >>> board = make_move(board, rows, columns, 2, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'X')
    False
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'X')
    True
    >>> check_win_row(board, rows, columns, 4, 3, 'X')    # A win depends on the value of num_connect
    False
    >>> check_win_row(board, rows, columns, num_connect, 3, 'O')   # We only detect wins for the given player
    False
    """
    "*** YOUR CODE HERE ***"
    adjacent = 0
    for col in range(max_cols):
        elem = get_piece(board, row, col)
        if elem != player:  # If two element of player is are separated, reset adjacent
            adjacent = 0
        else:
            adjacent += 1
        if adjacent >= num_connect:  # Return True immediately in case there are other elements left
            return True
    return False

def check_win_column(board, max_rows, max_cols, num_connect, col, player):
    """ Returns True if the given player has a vertical win in the given column,
    and otherwise False.

    >>> rows, columns, num_connect = 5, 5, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 0, 'X')
    False
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 1, 'O')
    False
    >>> board = make_move(board, rows, columns, 2, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 1, 'O')
    True
    >>> check_win_column(board, rows, columns, 4, 1, 'O')
    False
    >>> check_win_column(board, rows, columns, num_connect, 1, 'X')
    False
    """
    "*** YOUR CODE HERE ***"
    adjacent = 0
    for row in range(max_rows):
        elem = get_piece(board, row, col)
        if elem != player:  # If two element of player is are separated, reset num
            adjacent = 0
        else:
            adjacent += 1
        if adjacent >= num_connect:  # Return True immediately in case there are other elements left
            return True
    return False

def check_win(board, max_rows, max_cols, num_connect, row, col, player):
    """Returns True if the given player has any kind of win after placing a
    piece at (row, col), and False otherwise.

    >>> rows, columns, num_connect = 2, 2, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'O')
    False
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    True

    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 1, 0, 'X')
    True
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    False

    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    False
    >>> check_win(board, rows, columns, num_connect, 1, 0, 'X')
    True
    """
    diagonal_win = check_win_diagonal(board, max_rows, max_cols, num_connect,
                                      row, col, player)
    "*** YOUR CODE HERE ***"
    return check_win_row(board, max_rows, max_cols, num_connect, row, player) or \
        check_win_column(board, max_rows, max_cols, num_connect, col, player) or diagonal_win

###############################################################
### Functions for reference when solving the other problems ###
###############################################################

def check_win_diagonal(board, max_rows, max_cols, num_connect, row, col, player):
    """ Returns True if the given player has a diagonal win passing the spot
    (row, column), and False otherwise.
    """
    # Find top left of diagonal passing through the newly placed piece.
    adjacent = 0
    row_top_left, col_top_left = row, col
    while row_top_left > 0 and col_top_left > 0:
        row_top_left -= 1
        col_top_left -= 1

    # Loop through top left to bottom right diagonal and check for win.
    while row_top_left < max_rows and col_top_left < max_cols:
        piece = get_piece(board, row_top_left, col_top_left)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_left += 1
        col_top_left += 1

    # Find top right of diagonal passing through the newly placed piece.
    adjacent = 0
    row_top_right, col_top_right = row, col
    while row_top_right > 0 and col_top_right < max_cols - 1:
        row_top_right -= 1
        col_top_right += 1

    # Loop through top right to bottom left diagonal and check for win.
    while row_top_right < max_rows and col_top_right >= 0:
        piece = get_piece(board, row_top_right, col_top_right)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_right += 1
        col_top_right -= 1

    return False

#####################################################################################
### You do not need to read or understand the following code for this assignment. ###
#####################################################################################

import sys

def other(player):
    """ Returns the given player's opponent.
    """
    if player == 'X':
        return 'O'
    return 'X'

def play(board, max_rows, max_cols, num_connect):
    max_turns = max_rows * max_cols
    playing = True
    print("Player 'X' starts")
    who = 'X'
    turns = 0

    while True:
        turns += 1
        if turns > max_turns:
            print("No more moves. It's a tie!")
            sys.exit()

        while True:
            try:
                col_index = int(input('Which column, player {}? '.format(who)))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue

            row_index, board = make_move(board, max_rows, max_cols, col_index, who)

            if row_index != -1:
                break

            print("Oops, you can't put a piece there")

        print_board(board, max_rows, max_cols)

        if check_win(board, max_rows, max_cols, num_connect, row_index, col_index, who):
            print("Player {} wins!".format(who))
            sys.exit()

        who = other(who)

def start_game():
    # Get all parameters for the game from user.
    while True:
        # Get num_connect from user.
        while True:
            try:
                num_connect = int(input('How many to connect (e.g. 4 for Connect 4)? '))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue
            break

        # Get number of rows for board from user.
        while True:
            try:
                 max_rows = int(input('How many rows? '))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue
            break

        # Get number of columns for board from user.
        while True:
            try:
                max_cols = int(input('How many columns? '))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue
            break

        if max_rows >= num_connect or max_cols >= num_connect:
            break
        print("Invalid dimensions for connect {0}. Please try again.".format(num_connect))

    board = create_board(max_rows, max_cols)
    play(board, max_rows, max_cols, num_connect)