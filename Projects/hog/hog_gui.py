"""A graphical user interface (GUI) for the game of Hog.

This file uses many features of Python not yet covered in the course.
"""

from tkinter import *
import argparse
import sys
import tkinter as tk

import hog
import dice
from ucb import main


#############
# Utilities #
#############

class BetterWidget(object):
    """A BetterWidget returns itself on pack and config for call chaining."""
    def pack(self, **kwargs):
        super().pack(**kwargs)
        return self

    def config(self, **kwargs):
        super().config(**kwargs)
        return self

class TextWidget(BetterWidget):
    """A TextWidget contains a mutable line of text."""
    def __init__(self, **kwargs):
        self.textvar = kwargs.get('textvariable', tk.StringVar())
        self.config(textvariable=self.textvar)
        if 'text' in kwargs:
            self.textvar.set(kwargs['text'])

    @property
    def text(self):
        return self.textvar.get()

    @text.setter
    def text(self, value):
        return self.textvar.set(str(value))

class Text(tk.Text):
    """A Text is a text box."""
    def __init__(self, parent, **kwargs):
        kwargs.update(text_theme)
        tk.Text.__init__(self, parent, **kwargs)

class Label(TextWidget, tk.Label):
    """A Label is a text label."""
    def __init__(self, parent, **kwargs):
        kwargs.update(label_theme)
        tk.Label.__init__(self, parent, **kwargs)
        TextWidget.__init__(self, **kwargs)

class Button(BetterWidget, tk.Button):
    """A Button is an interactive button."""
    def __init__(self, *args, **kwargs):
        kwargs.update(button_theme)
        tk.Button.__init__(self, *args, **kwargs)

class Entry(TextWidget, tk.Entry):
    """An Entry widget accepts text entry."""
    def __init__(self, parent, **kwargs):
        kwargs.update(entry_theme)
        tk.Entry.__init__(self, parent, **kwargs)
        TextWidget.__init__(self, **kwargs)

class Frame(BetterWidget, tk.Frame):
    """A Frame contains other widgets."""
    def __init__(self, *args, **kwargs):
        kwargs.update(frame_theme)
        tk.Frame.__init__(self, *args, **kwargs)

class IORedirector(object):
    """A general class for redirecting I/O to this Text widget."""
    def __init__(self, text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):
    """A class for redirecting stdout to this Text widget."""
    def write(self, text):
        self.text_area.insert(END, text)
        self.text_area.see(END)

    def flush(self):
        pass  # No-op to prevent crash (https://stackoverflow.com/a/43014145).

def name(who):
    """Return the name of a player."""
    return "Player {0}".format(who)

#######
# GUI #
#######

class HogGUIException(BaseException):
    """HogGUI-specific Exception. Used to exit a game prematurely."""
    pass

class HogGUI(Frame):
    """Tkinter GUI for Hog."""

    KILL = -9   # kill signal to stop a game

    #########################
    # Widget Initialization #
    #########################

    def __init__(self, parent, computer=False):
        """Replace hog module's dice with hooks to GUI and start a game.

        parent   -- parent widget (should be root)
        computer -- True if playing against a computer
        """
        super().__init__(parent)
        self.pack(fill=BOTH)
        self.parent = parent
        self.who = 0

        self.init_scores()
        self.init_rolls()
        self.init_dice()
        self.init_status()
        self.init_messages()
        self.init_restart()

        self.computer, self.turn = computer, 0
        self.play()

    def init_scores(self):
        """Creates child widgets associated with scoring.

        Each player has a score Label that is updated each turn. Scores can be
        accessed and modified through Tkinter variables in self.score_vars.
        """
        self.score_frame = Frame(self).pack()

        self.p_frames = [None, None]
        self.p_labels = [None, None]
        self.s_labels = [None, None]
        for i in (0, 1):
            self.p_frames[i] = Frame(self.score_frame, padx=25).pack(side=LEFT)
            self.p_labels[i] = Label(self.p_frames[i],
                        text=name(i) + ':').pack()
            self.s_labels[i] = Label(self.p_frames[i]).pack()

    def init_rolls(self):
        """Creates child widgets associated with the number of rolls.

        The primary widget is an Entry that accepts user input. An intermediate
        Tkinter variable, self.roll_verified, is set to the final number of
        rolls. Once it is updated, the player immediately takes a turn based on
        its value.
        """
        self.roll_frame = Frame(self).pack()

        self.roll_label = Label(self.roll_frame).pack()
        self.roll_entry = Entry(self.roll_frame,
                                justify=CENTER).pack()
        self.roll_entry.bind('<Return>',
                             lambda event: self.roll_button.invoke())
        self.roll_verified = IntVar()
        self.roll_button = Button(self.roll_frame,
                                  text='Roll!',
                                  command=self.roll).pack()

    def init_dice(self):
        """Creates child widgets associated with dice. Each dice is stored in a
        Label. Dice Labels will be packed or unpacked depending on how many dice
        are rolled.
        """
        self.dice_frames = [
            Frame(self).pack(),
            Frame(self).pack(),
            Frame(self).pack(),
            Frame(self).pack()
        ]
        self.dice = {
            i: Label(self.dice_frames[i//5]).
                    config(image=HogGUI.IMAGES[6]).
                    pack(side=LEFT)
            for i in range(10)
        }

    def init_status(self):
        """Creates child widgets associated with the game status. For example,
        Hog Wild is displayed here."""
        self.status_label = Label(self).pack()

    def init_messages(self):
        """Creates child widgets associated with game messages."""
        self.messages = Text(self)
        self.messages.pack()
        sys.stdout = StdoutRedirector(self.messages)

    def init_restart(self):
        """Creates child widgets associated with restarting the game."""
        self.restart_button = Button(self, text='Restart',
                                     command=self.restart).pack()

    ##############
    # Game Logic #
    ##############

    def make_dice(self, sides):
        """Creates a dice function that hooks to the GUI and wraps
        dice.make_fair_dice.

        sides -- number of sides for the die
        """
        fair_dice = dice.make_fair_dice(sides)
        def gui_dice():
            """Roll fair_dice and add a corresponding image to self.dice."""
            result = fair_dice()
            img = HogGUI.IMAGES[result]
            self.dice[self.dice_count].config(image=img).pack(side=LEFT)
            self.dice_count += 1
            return result
        return gui_dice

    def clear_dice(self):
        """Unpacks (hides) all dice Labels."""
        for i in range(10):
            self.dice[i].pack_forget()

    def clear_messages(self):
        self.messages.delete(1.0, END)

    def roll(self):
        """Verify and set the number of rolls based on user input. As
        per game rules, a valid number of rolls must be an integer
        greater than or equal to 0.
        """
        self.clear_messages()
        result = self.roll_entry.text
        try:
            rolls = 10 >= int(result) >= 0
            assert rolls, 'Rolls must be between 0 and 10, inclusive'
            self.roll_verified.set(int(result))
        except (ValueError, AssertionError) as e:
            print(e)

    def switch(self, who=None):
        """Switches players. self.who is either 0 or 1."""
        self.p_frames[self.who].config(bg=bg)
        self.p_labels[self.who].config(bg=bg)
        self.s_labels[self.who].config(bg=bg)
        self.who = 1 - self.who if who is None else who
        self.p_frames[self.who].config(bg=select_bg)
        self.p_labels[self.who].config(bg=select_bg)
        self.s_labels[self.who].config(bg=select_bg)

    def strategy(self, score, opp_score):
        """A strategy with a hook to the GUI. This strategy gets
        passed into the PLAY function from the HOG module. At its
        core, the strategy waits until a number of rolls has been
        verified, then returns that number. Game information is
        updated as well.

        score     -- player's score
        opp_score -- opponent's score
        """
        s0 = score if self.who == 0 else opp_score
        s1 = opp_score if self.who == 0 else score
        self.s_labels[0].text = s0
        self.s_labels[1].text = s1
        self.roll_label.text = name(self.who) +' will roll:'
        status = self.status_label.text
        self.status_label.text = status

        if self.computer and self.who == self.turn:
            self.update()
            self.after(DELAY)
            result = hog.final_strategy(score, opp_score)
        else:
            self.roll_entry.focus_set()
            self.wait_variable(self.roll_verified)
            result = self.roll_verified.get()
            self.roll_entry.text = ''
        if result == HogGUI.KILL:
            raise HogGUIException

        self.clear_dice()
        self.dice_count = 0
        self.status_label.text = '{} chose to roll {}.'.format(name(self.who),
                                                               result)
        self.switch()
        return result

    def play(self):
        """Simulates a game of Hog by calling hog.play with the GUI strategies.

        If the player destroys the window prematurely (i.e. in the
        middle of a game), a HogGUIException is raised to exit out
        of play's loop. Otherwise, the widget will be destroyed,
        but the strategy will continue waiting.
        """
        self.turn = 1 - self.turn
        self.switch(0)
        self.s_labels[0].text = '0'
        self.s_labels[1].text = '0'
        self.status_label.text = ''
        try:
            commentary = hog.both(hog.announce_highest(0),
                         hog.both(hog.announce_highest(1),
                                  hog.announce_lead_changes()))
            score, opponent_score = hog.play(self.strategy,
                                             self.strategy,
                                             dice=self.make_dice(6),
                                             say=commentary)
        except HogGUIException:
            pass
        else:
            self.s_labels[0].text = score
            self.s_labels[1].text = opponent_score
            winner = 0 if score > opponent_score else 1
            self.status_label.text = 'Game over! {} wins!'.format(
                                        name(winner))

    def restart(self):
        """Kills the current game and begins another game."""
        self.roll_verified.set(HogGUI.KILL)
        self.status_label.text = ''
        self.clear_dice()
        self.clear_messages()
        self.play()

    def destroy(self):
        """Overrides the destroy method to end the current game."""
        self.roll_verified.set(HogGUI.KILL)
        super().destroy()

def run_GUI(computer=False):
    """Start the GUI.

    computer -- True if playing against computer
    """
    root = Tk()
    root.title('The Game of Hog')
    root.minsize(520, 600)
    root.geometry("520x600")

    # Tkinter only works with GIFs
    HogGUI.IMAGES = {
        1: PhotoImage(file='images/die1.gif'),
        2: PhotoImage(file='images/die2.gif'),
        3: PhotoImage(file='images/die3.gif'),
        4: PhotoImage(file='images/die4.gif'),
        5: PhotoImage(file='images/die5.gif'),
        6: PhotoImage(file='images/die6.gif'),
    }

    app = HogGUI(root, computer)
    root.mainloop()

##########
# THEMES #
##########

select_bg = '#a6d785'
bg='#ffffff'
fg='#000000'
font=('Arial', 14)
height=5  # Lines

frame_theme = {
    'bg': bg,
}

label_theme = {
    'font': font,
    'bg': bg,
    'fg': fg,
}

text_theme = {
    'font': font,
    'bg': bg,
    'fg': fg,
    'height': height,
}

button_theme = {
    'font': font,
    'activebackground': select_bg,
    'bg': bg,
    'fg': fg,
}

entry_theme = {
    'fg': fg,
    'bg': bg,
    'font': font,
    'insertbackground': fg,
}

##########################
# Command Line Interface #
##########################

DELAY=2000

@main
def run(*args):
    parser = argparse.ArgumentParser(description='Hog GUI')
    parser.add_argument('-f', '--final',
                        help='play against the final strategy in hog.py. '
                             'Computer alternates playing as player 0 and 1.',
                        action='store_true')
    parser.add_argument('-d', '--delay',
                        help='time delay for computer, in seconds', type=int,
                        default=2)
    args = parser.parse_args()
    global DELAY
    DELAY = args.delay * 1000
    run_GUI(computer=args.final)