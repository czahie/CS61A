# CS 61A World Game Data:
from classes import *

# Characters:

james = Character('James',
                  'I saw Gibbes near Soda with a smoothie. You can probably find him there.')
gibbes = Character('Gibbes',
                 "This smoothie is so disappointing! "
                 "I wish someone would bring me a non-disappointing smoothie.")
jen = Character('Jen',
                  'No one brought food to the potluck! '
                  'Maybe the Golden Bear Cafe (GBC) is open; we can get food there.')
jerry_113 = Character('Jerry',
                     "You just saw me in Wheeler? But I've been here all along!")
tiffany = Character('Tiffany',
                 "My marker ran out of ink, so I can't vandalize this tower!")
jerry = Character('Jerry',
                  'I heard you like games, so I put some games in this game. '
                  'Have you gone to Games of Berkeley on Shattuck?')
allen = Character('Allen',
                  'Hey! Want to play ultimate frisbee?')
student = Character('Student',
                    'I once went into Dwinelle and got lost for 3 days! '
                    'That place is a maze!')
scared_student = Character('Terrified Student',
                           "I've been lost in Dwinelle for weeks")
spooked_student = Character('Spooked Student',
                            'Help')

# Things:
smoothie = Thing('Smoothie',
               "Looks pretty non-disappointing. Gibbes might want this.")
lemon = Thing('Lemon',
               'Hmmm... try bringing it to a TA')
coffee = Thing('Coffee',
               'The sweet, caffeinated nectar of the gods')
monopoly = Thing('Monopoly',
              'Just right for 61A study breaks!')
strange_skull = Thing('Strange Skull',
                      'A strange skull. Dinosaur? Giraffe? Who knows.')

# Keys:
try:
    skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors')
except NameError as e:
    skeleton_key = Thing('Not a Skeleton Key', 'You must first implement the Key class')

# Places:

sather_gate = Place('Sather Gate', 'Sather Gate - A fairly ineffective gate',
                    [], [])
fsm = Place('FSM', 'Free Speech Cafe - Home of Coffee',
            [], [smoothie, coffee])
vlsb = Place('VLSB', 'VLSB - Have you visited the dinosaur?',
             [james], [skeleton_key])
soda = Place('Soda', 'Soda Hall - A building where Soda is not allowed',
             [gibbes, jen, jerry_113], [])
gbc = Place('GBC', 'Golden Bear Cafe - Now with (healthy?) food',
            [], [lemon])
campanile = Place('Campanile', 'The Campanile - A great tower!',
                  [tiffany], [])
game_store = Place('Games of Berkeley', 'Games of Berkeley',
                   [], [monopoly])
hp = Place('HP', 'HP Auditorium',
            [], [])
shattuck = Place('Shattuck', 'Shattuck Avenue',
                 [], [])
wheeler = Place('Wheeler', 'Wheeler - CS61A lectures are held here.',
                [jerry], [])
dwinelle = Place('Dwinelle Hall', 'Dwinelle Hall - A Maze',
                 [student], [])
deep_dwinelle = Place('Deep in Dwinelle Hall', 'You are lost in Dwinelle Hall',
                      [scared_student, spooked_student], [strange_skull])
memorial_glade = Place('Memorial Glade', 'Memorial Glade on a beautiful day',
                       [allen], [])


# Exits:
sather_gate.add_exits([gbc, wheeler, dwinelle, memorial_glade])
gbc.add_exits([sather_gate])
wheeler.add_exits([sather_gate, campanile])
deep_dwinelle.add_exits([deep_dwinelle, dwinelle])
dwinelle.add_exits([sather_gate, vlsb, wheeler, deep_dwinelle])
memorial_glade.add_exits([sather_gate, fsm, campanile, soda])
campanile.add_exits([memorial_glade, wheeler])
vlsb.add_exits([fsm, soda, shattuck, dwinelle])
shattuck.add_exits([vlsb, game_store])
fsm.add_exits([vlsb, memorial_glade])
soda.add_exits([hp, vlsb, memorial_glade])
hp.add_exits([soda])
game_store.add_exits([shattuck])

# Locked Buildings
fsm.locked = True

# Player:
# The Player should start at sather_gate.
me = Player('Joe', sather_gate)
