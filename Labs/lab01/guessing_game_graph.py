"""Guessing Game Visualization

You do not need to understand any of the code in this file.
"""

# This section avoids asking for user input.

def prompt_for_number(lower, upper):
    from random import randint
    prompt_for_number.number = randint(lower, upper)
    return prompt_for_number.number

def is_correct(guess):
    return guess == prompt_for_number.number

def is_too_high(guess):
    return guess > prompt_for_number.number

import lab01_extra
lab01_extra.LOWER = 1
lab01_extra.UPPER = 100
lab01_extra.prompt_for_number = prompt_for_number
lab01_extra.is_correct = is_correct
lab01_extra.is_too_high = is_too_high

# This section runs an algorithm many times.

from collections import defaultdict
import sys
import webbrowser

def get_frequency(algorithm_name, runs=1000):
    """Collect frequencies and plot them."""
    if not hasattr(lab01_extra, algorithm_name):
        raise ValueError('invalid guessing algorithm ({0})'.format(algorithm_name))
    algorithm = getattr(lab01_extra, algorithm_name)

    counts = defaultdict(int)
    for i in range(runs):
        num_guesses = algorithm()
        counts[num_guesses] += 1

    most_guesses = max(counts)
    if most_guesses == 1:
        raise ValueError('num_guesses was always 1. Make sure your functions '
                         'are returning the correct number of guesses!')
    xs = range(1, most_guesses+1)
    ys = [sum(counts[i] for i in range(1, x+1)) for x in xs]

    if algorithm_name == 'guess_binary':
        x_axis_string = '|'.join(map(str, xs))
        y_axis_string = ','.join(map(str, ys))
        chxp = ','.join(map(str, range(int(100 / 2 / most_guesses)+1, 100, int(100 / most_guesses))))
        data_string = 'chd=t:{0}&chxl=0:|{1}|2:|Max number of guesses|3:|Frequency|&chxp=0,{3}|2,50|3,{2}'.format(y_axis_string, x_axis_string, runs/2, chxp)
    else:
        step = max(most_guesses // 10, 1)
        x_axis_string = '|'.join(map(str, range(0, most_guesses+1, step)))
        y_axis_string = ','.join(map(str, ys))
        data_string = 'chd=t:{0}&chxl=0:|{1}|2:|Max number of guesses|3:|Frequency|&chxp=0,0|2,50|3,{2}'.format(y_axis_string, x_axis_string, runs/2)
    url = 'http://chart.googleapis.com/chart?cht=bvg&chtt={0}&chxt=x,y,x,y&chs=500x500&{1}&chds=a&chco=3072F3&chbh=a&chm=s,000000,0,-1,5|s,000000,1,-1,5&chdlp=l'.format(algorithm_name, data_string)

    webbrowser.open_new(url)

if __name__ == "__main__":
    file_name, algorithm_name = sys.argv
    get_frequency(algorithm_name)