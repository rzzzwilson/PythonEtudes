"""
This experimental code is trying to implement a simple text adventure.

We just have static data structures describing places.  The player may
move around with the usual commands and pick up/drop objects.

We change TextAdventure.01.py to:

* have objects that may be picked up and dropped
* allow Places to contain objects
"""

class Place:
    """A Place in the text adventure."""

    def __init__(self, name, description, connections, long_description=None):
        self.name = name
        self.description = description
        self.connections = connections
        self.long_description = description
        if long_description:
            self.long_description = long_description
        self.objects = []

    def __str__(self):
        """For debug."""

        return f"Place('{self.name}')"

class Object:
    """An object."""

    def __init__(self, name, description, place, long_description=None):
        self.name = name
        self.description = description
        self.initial_place = place
        self.long_description = description
        if long_description:
            self.long_description = long_description

    def __str__(self):
        """For debug."""

        return f"Object('{self.name}')"


# the Places in this adventure
white_house = Place('white_house', 'at the White house.',
                    connections={'east': 'path',
                                 'south': 'forest'},
                    long_description=('at the White house. '
                                      'Paths lead south and east from here.'))

path = Place('path', 'on a narrow east-west path.',
             connections={'east': 'glade',
                          'west': 'white_house'})

glade = Place('glade', 'in a shadowed glade.',
              connections={'west': 'path',
                           'southwest': 'forest'},
              long_description=('in a shadowed glade, '
                                'with paths to the west and southwest.'))

forest = Place('forest', 'in a dark difficult forest.',
               connections={'northeast': 'glade',
                            'north': 'white_house'},
               long_description=('in a dark difficult forest. '
                                 'Narrow tracks go northeast and north.'))

# the objects in this adventure
axe = Object('axe', 'a small Elvish axe.', 'glade',
             long_description=('a small Elvish axe. '
                               'There are faint unreadable engravings on the head.'))

# dynamically populate the "place_name_ref" and "object_name_ref" dictionaries
# also check that unique name strings actually are UNIQUE!
place_name_ref = {}
object_name_ref = {}
for (obj_name, obj) in globals().copy().items():
    if isinstance(obj, Place):
        name = obj.name
        if name in place_name_ref:      # check unique name is unique
            msg = f"Place in variable '{obj_name}' doesn't have a unique identifier: '{name}'"
            raise ValueError(msg)
        place_name_ref[name] = obj
    elif isinstance(obj, Object):
        name = obj.name
        if name in object_name_ref:     # check unique name is unique
            msg = f"Object in variable '{obj_name}' doesn't have a unique identifier: '{name}'"
            raise ValueError(msg)
        object_name_ref[name] = obj

        # place Object into the required Place
        place = obj.initial_place
        place_ref = globals()[place]
        place_ref.objects.append(name)
        print(f'Placed Object {name} into {place_ref}')
        
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

    previous_places.insert(0, place)
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

    # if there's something here, print its/their description
    if place.objects:
        print('\nYou see here:')
        for obj_name in place.objects:
            print(f'\t{object_name_ref[obj_name].description}')

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
        current_place = place_name_ref[current_place.connections[cmd]]
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
