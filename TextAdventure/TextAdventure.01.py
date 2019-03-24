"""
This experimental code is trying to implement a simple text adventure.

We just have static data structures describing places.  The player may
move around with the usual commands.

We change TextAdventure.0.py to have:

* a nicer 'quit' command to stop playing
* a 'look' command to redescribe the current Place
* automatic population of the "name_place" dictionary mapping the unique
  place identifier string to the Place instance
* code that displays a place "long description" if we are new to the Place,
  but displays a short description if we return to a Place we just left
"""

class Place:
    """A Place in the text adventure."""

    def __init__(self, name, description, connections, long_description=None):
        self.name = name
        self.description = description
        self.connections = connections
        if long_description is None:
            long_description = description
        self.long_description = long_description

    def __str__(self):
        """For debug."""

        return f"Place('{self.name}')"

# the Places in this adventure
white_house = Place('white_house', 'at the White house.',
                    connections={'east': 'path',
                                 'south': 'forest'},
                    long_description='at the White house. Paths lead south and east from here.')

path = Place('path', 'on a narrow path.',
             connections={'east': 'glade',
                          'west': 'white_house'})

glade = Place('glade', 'in a shadowed glade.',
              connections={'west': 'path',
                           'southwest': 'forest'},
              long_description='in a shadowed glade, with paths to the west and southwest.')

forest = Place('forest', 'in a dark difficult forest.',
               connections={'northeast': 'glade',
                            'north': 'white_house'},
               long_description='in a dark difficult forest.  Narrow tracks go northeast and north.')

# dynamically populate the "name_place"
# dictionary with unique Place identifying string mapping to the Place instance
name_place = {}
for obj_name in locals().copy():     # must work on copy of locals() result
    obj = locals()[obj_name]
    if isinstance(obj, Place):
        name_place[obj_name] = obj

# map allowed input moves to "canonical" move strings
allowed_commands = {'north': 'north', 'n': 'north',
                 'northeast': 'northeast', 'ne': 'northeast',
                 'east': 'east', 'e': 'east',
                 'southeast': 'southeast', 'se': 'southeast',
                 'south': 'south', 's': 'south',
                 'southwest': 'southwest', 'sw': 'southwest',
                 'west': 'west', 'w': 'west',
                 'northwest': 'northwest', 'nw': 'northwest',
                 'quit': 'quit', 'q': 'quit', 'ex': 'quit', 'exit': 'quit',
                 'stop': 'quit', 'leave': 'quit',
                 'look': 'look', 'l': 'look',
                }

# the "current" place, ie, where the player is
current_place = white_house

# the previous Place, used to implement the "short" description on revisit
previous_place = None

def describe_place(place):
    """Describe the current place.
    
    place  a reference to the Place() object to describe
    """

    if place != previous_place:
        print('You are ' + place.long_description)
    else:
        print('You are ' + place.description)

def get_command():
    """Get a legal command.
   
    Accepts any of the allowed commands even if it won't work
    in the current Place.

    Returns the canonical command string.
    """

    while True:
        cmd = input('What do you want to do? ').lower()
        try:
            return allowed_commands[cmd]
        except KeyError:
            print(f"Sorry, '{cmd}' isn't a legal command here.  Try again.\n")

def do_command(cmd):
    """Check if the command is legal in the current Place.  If so, do it.

    cmd  the canonical command string

    Returns True if command allowed.  "current_place" is updated.
    Returns False if command not allowed.
    """

    global current_place
    global previous_place

    if cmd in current_place.connections:
        new_place = name_place[current_place.connections[cmd]]
        (previous_place, current_place) = (current_place, new_place)
        return True

    return False


# play the game
while True:
    describe_place(current_place)
    cmd = get_command()
    if cmd == 'quit':
        break
    if cmd == 'look':
        previous_place = None
        continue
    if not do_command(cmd):
        print("Sorry, you can't do that.  Try again.\n")

print('So long.')
