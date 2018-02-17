from lab05 import *
## Optional Questions ##

# pyTunes (optional)

def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> country_tunes = tree('country_tunes',
    ...                  [tree('country',
    ...                    [tree('jason aldean',
    ...                       [tree('johnny cash')]),
    ...                     tree('johnny cash',
    ...                       [tree('hurt')])])])
    >>> new_country = add_song(country_tunes, 'ring of fire', 'johnny cash')
    >>> print_tree(new_country)
    country_tunes
      country
        jason aldean
          johnny cash
        johnny cash
          hurt
          ring of fire
    """
    "*** YOUR CODE HERE ***"
# My solution
    if is_leaf(t):  # You cannot add a song under a song
        return t
    elif label(t) == category:  # Add the song
        return tree(label(t), branches(t) + [tree(song)])
    else:
        return tree(label(t),[add_song(b, song, category) for b in branches(t)])

# Official solution1
    if label(t) == category and not is_leaf(t):
        return tree(label(t), branches(t) + [tree(song)])
    kept_branches = []
    for b in branches(t):
        kept_branches += [add_song(b, song, category)]
    return tree(label(t), kept_branches)

# Official solution2
    if label(t) == category and not is_leaf(t):
        return tree(label(t), branches(t) + [tree(song)])
    all_branches = [add_song(b, song, category) for b in branches(t)]
    return tree(label(t), all_branches)

def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    "*** YOUR CODE HERE ***"
# My solution, which may have some small bugs
    if label(t) == target:
        return []
    delete_branches = branches(t)
    for b in branches(t):
        if label(b) == target:
            delete_branches.remove(b)
        else:
            delete(b, target)
    return tree(label(t), delete_branches)

# Official solution1
    kept_branches = []
    for b in branches(t):
        if label(b) != target:
            kept_branches += [delete(b, target)]
    return tree(label(t), kept_branches)

# Official solution2
    kept_branches = [delete(b, target) for b in branches(t) if label(b) != target]
    return tree(label(t), kept_branches)


# Shakespeare and Dictionaries
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table.setdefault(prev, [])
        table[prev].append(word)
        prev = word
    return table

def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
    return result + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)
