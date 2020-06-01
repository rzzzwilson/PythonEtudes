"""
This experimental code is trying to implement a simple text adventure.

We just have static data structures describing places.  The player may
move around with the usual commands.

We change TextAdventure.00.py to have:

* a nicer 'quit' command to stop playing
* code that displays a place "long description" if we are new to the Place,
  but displays a short description if we return to a Place we just left
* a 'look' command to redescribe the current Place (long description)
* automatic population of the "name_place" dictionary mapping the unique
  place identifier string to the Place instance
"""

class Place:
    """A Place in the text adventure."""

    def __init__(self, name, description, connections, long_description=None):
        self.name = name
        self.description = description
        self.connections = connections
        self.long_description = description     # just in case no long description
        if long_description:
            self.long_description = long_description

    def __str__(self):
        """For debug."""

        return f"Place('{self.name}')"

# the Places in this adventure
white_house = Place('white_house', 'at the White house.',
                    connections={'east': 'path',
                                 'south': 'forest'},
                    long_description='at the White house. Paths lead south and east from here.')

path = Place('path', 'on a narrow east-west path.',
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

# dynamically populate the "name_place" dictionary with unique Place identifying
# string mapping to the Place instance.
# also check that unique name strings actually are UNIQUE!
name_place = {}
for (obj_name, obj) in globals().copy().items():    # MUST USE copy()!
    if isinstance(obj, Place):
        name = obj.name
        if name in name_place:      # check unique name is unique
            msg = f"Place in variable '{obj_name}' doesn't have a unique identifier: '{name}'"
            raise ValueError(msg)
        name_place[name] = obj

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
previous_places = []
num_previous = 4    # the number of previous places to remember in "previous_places"

def push_prev(place):
    """Push a place onto the "previous_places" list.

    place  the place to push

    Oldest entries are deleted to limit list to "num_previous" entries.
    """

    previous_places.insert(0, place)        # new place inserted at left
    del previous_places[num_previous:]

def describe_place(place, look=False):
    """Describe the current place.
    
    place  a reference to the Place() object to describe
    look   if True, print long description
    """

    if look or place not in previous_places[1:]:
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

    if cmd in current_place.connections:
        current_place = name_place[current_place.connections[cmd]]
        push_prev(current_place)
        return True

    return False


# play the game
force_look = False
push_prev(current_place)    # start at the "current_place"
while True:
    describe_place(current_place, look=force_look)
    force_look = False
    cmd = get_command()
    if cmd == 'quit':
        break
    if cmd == 'look':
        force_look = True
        continue
    if not do_command(cmd):
        print("Sorry, you can't do that.  Try again.\n")

print('So long.')
