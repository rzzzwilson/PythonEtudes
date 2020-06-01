"""
This experimental code is trying to implement a simple text adventure.

We just have static data structures describing places.  The player may
move around with the usual commands.

We change TextAdventure.3.py to:

* create a Monster object
* the Monster object may move around the map
* to see Monster movement, allow the user 'wait' command
"""

import random

class Place:
    """A Place in the text adventure."""

    def __init__(self, name, description, connections, long_description=None):
        self.name = name
        self.description = description
        self.connections = connections
        if long_description is None:
            long_description = description
        self.long_description = long_description
        self.objects = []

    def __str__(self):
        """For debug."""

        return f"Place('{self.name}')"

class Object:
    """An object."""

    def __init__(self, name, description, long_description=None):
        self.name = name
        self.description = description
        if long_description is None:
            long_description = description
        self.long_description = long_description

    def __str__(self):
        """For debug."""

        return f"Object('{self.name}')"

class Player:
    """An object to hold player information."""

    def __init__(self, name):
        self.name = name
        self.inventory = []

    def __str__(self):
        """For debug."""

        return f"Player('{self.name}')"

class Monster:
    """A monster object."""

    def __init__(self, name, description, place):
        self.name = name
        self.description = description

    def move(self):
        """The monster moves in a random direction about 50% of the time."""

        # decide if monster moves
        if random.random() < 0.5:
            return      # no move this turn

        # look at the current "place" for possible moves, pick one
        place = monster_name_place[self.name]
        place_ref = place_name_ref[place]
        direction = random.choice(list(place_ref.connections.keys()))

        # figure out where that leads to and move
        new_place = place_ref.connections[direction]
        new_place_ref = place_name_ref[new_place]
        monster_name_place[self.name] = new_place

    def __str__(self):
        """For debug."""

        return f"Monster('{self.name}')"


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
axe = Object('axe', 'a small Elvish axe',
             long_description=('a small Elvish axe. '
                               'There are faint unreadable engravings on the head.'))

# this dictionary maps an object to the Place it initially appears in
object_initial_places = {'axe': 'glade'}

# the monsters in this map
goblin = Monster('goblin', 'A hairy goblin with very bad breath', 'glade')

# this dictionary maps a Monster object to the Place it initially appears in
monster_initial_places = {'goblin': 'glade'}

# dynamically populate the "place_name_ref" dictionary with unique Place identifying
# string mapping to the Place instance.
# also check that unique name strings actually are UNIQUE!
place_name_ref = {}
for (obj_name, obj) in globals().copy().items():
    if isinstance(obj, Place):
        name = obj.name
        if name in place_name_ref:      # check unique name is unique
            msg = f"Place in variable '{obj_name}' doesn't have a unique identifier: '{name}'"
            raise ValueError(msg)
        place_name_ref[name] = obj

# code to place all objects in their initial position in the map
# we also need to populate the "object_name_ref" ditionary
object_name_ref = {}
for (name, place) in object_initial_places.items():
    object_ref = globals()[name]
    object_name_ref[name] = object_ref
    place_ref = globals()[place]
    place_ref.objects.append(name)

# code to place all monsters in their initial position in the map
# we also need to populate the "monster_name_ref" ditionary
monster_name_place = {}     # map monster name to place string
monster_name_ref = {}       # map monster name to actual monster reference
for (name, place) in monster_initial_places.items():
    monster_ref = globals()[name]
    monster_name_ref[name] = monster_ref
    place_ref = globals()[place]
#    monster_name_place[name] = place_ref
    monster_name_place[name] = place

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
                    'get': 'get', 'g': 'get', 'pickup': 'get',
                    'drop': 'drop', 'd': 'drop',
                    'inventory': 'invent', 'inv': 'invent', 'i': 'invent',
                    'wait': 'wait', 'w': 'wait',
                   }

# we must map what the user might call an object to the "real" object name.
# this dictionary maps a user name to a list of actual object names
# whenever a user mentions a name like 'axe' we look through this dictionary
# and get a list of object ID strings that might be the user object
user_names_real = {'axe': ['axe'],
                  }

# the "current" place, ie, where the player is
current_place = white_house

# the previous Place, used to implement the "short" description on revisit
previous_places = []
num_previous = 3    # the number of previous places to remember in "previous_places"

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
        print(f"You are {place.long_description}")
    else:
        print(f"You are {place.description}")

    # if there's an object here, print its description
    if place.objects:
        print('\nYou see here:')
        for obj_name in place.objects:
            print(f'\t{object_name_ref[obj_name].description}')

    # if there are monsters here, print their descriptions
    place_name = place.name
    prefix = False
    for (monster_name, monster_place) in monster_name_place.items():
        if monster_place == place.name:
            if not prefix:
                print('\nYou see:')
                prefix = True
            monster_ref = monster_name_ref[monster_name]
            print(f'\t{monster_ref.description}')

def get_command():
    """Get a legal command.
   
    Accepts any of the allowed commands even if it won't work
    in the current Place.

    Returns the command as a tuple (verb, noun) where "verb" is a canonical
    command string and "noun" may be None or a string.
    """

    while True:
        cmd = input('What do you want to do? ').lower()
        try:
            (verb, noun) = cmd.split(maxsplit=1)
        except ValueError:
            verb = cmd      # only one word
            noun = None

        try:
            return (allowed_commands[verb], noun)
        except KeyError:
            print(f"Sorry, '{verb}' isn't a legal command here.  Try again.\n")

def drop_object(noun):
    """If object is in the player's inventory, drop it.

    noun  the noun string the user used
    """

    # is this noun one of the recognized nouns?
    if noun not in user_names_real:
        print(f"I don't know this '{noun}'.")
        return

    # see if an object matching the user name is in the player's inventory
    for obj_id in user_names_real[noun]:
        if obj_id in player.inventory:
            # object there, drop it
            player.inventory.remove(obj_id)
            current_place.objects.append(obj_id)
            print('Dropped.')
            return

    print(f"Sorry, you aren't carrying this: {noun}.")

def pickup_object(noun):
    """If object is in 'current_place' pickup object.

    noun  the noun string the user used
    """

    # is this noun one of the recognized nouns?
    if noun not in user_names_real:
        print(f"I don't know this '{noun}'.")
        return

    # see if an object matching the user name is in the current Place
    for obj_id in user_names_real[noun]:
        if obj_id in current_place.objects:
            # object here, take it
            current_place.objects.remove(obj_id)
            player.inventory.append(obj_id)
            print('Taken.')
            return

    print(f"Sorry, I see no {noun} here.")

def inventory():
    """Print the player's inventory."""

    if player.inventory:
        print('You are carrying:')
        for obj in player.inventory:
            print(f'\t{object_name_ref[obj].description}')
    else:
        print("You aren't carrying anything.")

def do_command(verb, noun=None):
    """Check if the command is legal in the current Place.  If so, do it.

    verb  the canonical command string
    noun  an optional object name the 'verb' verb applies to

    Returns True if command allowed.  "current_place" is updated if it's a move.
    Returns False if command not allowed.
    """

    global current_place

    # run through the list of action words
    if verb == 'get':
        # user wants to get something
        if noun is None:
            print("Sorry, you must use 'get' with a noun, like 'get axe'.")
        else:
            pickup_object(noun)
    elif verb == 'drop':
        # user wants to drop something
        if noun is None:
            print("Sorry, you must use 'drop' with a noun, like 'drop axe'.")
        else:
            drop_object(noun)
    elif verb == 'invent':
        if noun:
            # can't use a noun with "inventory"
            print("Sorry, the 'inventory' command doesn't take a second word.")
        else:
            inventory()
    elif verb == 'wait':
        if noun:
            # can't use a noun with "wait"
            print("Sorry, the 'wait' command doesn't take a second word.")
        else:
            print('Time passes...') # we do nothing, time passes
    else:
        # might be a move
        if verb in current_place.connections:
            current_place = place_name_ref[current_place.connections[verb]]
            push_prev(current_place)

def move_monsters():
    """Move all monsters in the map."""

    # iterate over all monster references and call ".move()"
    for monster_ref in monster_name_ref.values():
        monster_ref.move()

# play the game
force_look = False
push_prev(current_place)    # start at the "current_place"

player = Player('Fred')

while True:
    describe_place(current_place, look=force_look)
    force_look = False
    (verb, noun) = get_command()
    if verb == 'quit':
        break
    elif verb == 'look':
        force_look = True
    else:
        do_command(verb, noun)
    move_monsters()
    print()

print('So long.')
