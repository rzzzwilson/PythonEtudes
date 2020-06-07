"""
This experimental code is trying to implement a simple text adventure.

We change TextAdventure.04.py to:

* write data to a save file on shutdown.
"""

import json
import random

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
        self.monsters = []

    def state(self):
        """Return a "dictionary" description of the Place.

        Just enough to recreate the Place from saved data.
        "self.objects" & "self.monsters" will be filled in dynamically.
        """

        return {'name': self.name,
                'description': self.description,
                'connections': self.connections,
                'long_description': self.long_description,
               }
                
    def __str__(self):
        """For debug."""

        return f"Place('{self.name}')"

class Object:
    """An object."""

    def __init__(self, name, description, place, long_description=None):
        self.name = name
        self.description = description
        self.place = place
        self.long_description = description
        if long_description:
            self.long_description = long_description

    def state(self):
        """Return a "dictionary" description of the Object.

        Just enough to recreate the Object from saved data.
        """

        return {'name': self.name,
                'description': self.description,
                'place': self.place,
                'long_description': self.long_description,
               }
                
    def __str__(self):
        """For debug."""

        return f"Object('{self.name}')"

class Player:
    """An object to hold player information."""

    def __init__(self, name, inventory=None):
        self.name = name
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def state(self):
        """Return a "dictionary" description of the Player.

        Just enough to recreate the Player from saved data.
        "self.inventory" will be filled in dynamically.
        """

        return {'name': self.name,
                'inventory': self.inventory,
               }
                
    def __str__(self):
        """For debug."""

        return f"Player('{self.name}')"

class Monster:
    """A monster object."""

    def __init__(self, name, description, place):
        self.name = name
        self.description = description
        self.place = place

    def state(self):
        """Return a "dictionary" description of the Monster.

        Just enough to recreate the Monster from saved data.
        """

        return {'name': self.name,
                'description': self.description,
                'place': self.place,
               }

    def move(self):
        """The monster moves in a random direction about 50% of the time."""

        # decide if monster moves
        if random.random() < 0.5:
            return      # no move this turn

        # look at the current "place" for possible moves, pick one
        place = self.place
        place_ref = place_name_ref[place]
        direction = random.choice(list(place_ref.connections.keys()))

        # figure out where that leads to and move
        new_place = place_ref.connections[direction]
        new_place_ref = place_name_ref[new_place]
        place_ref.monsters.remove(self.name)
        new_place_ref.monsters.append(self.name)

        # finally, update self.place since that will be used when loading from file
        self.place = new_place

    def __str__(self):
        """For debug."""

        return f"Monster('{self.name}')"

#####
# Start of static data
#####

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

# the monsters in this adventure
goblin = Monster('goblin', 'A hairy goblin with very bad breath.', 'glade')

# the "current" place, ie, where the player is
current_place = white_house

# the Player instance
player = Player('Fred')

# populate "place_name_ref", "object_name_ref" & "monster_name_ref" dictionaries
# also check that unique name strings actually are UNIQUE!
# we do Places first, because Objects/Monsters need Places defined first.
place_name_ref = {}
for (obj_name, obj) in globals().copy().items():
    if obj_name == 'current_place':
        continue                        # skip "current_place"
    if isinstance(obj, Place):
        name = obj.name
        if name in place_name_ref:      # check unique name _is_ unique
            msg = f"Place in variable '{obj_name}' doesn't have a unique identifier: '{name}'"
            raise ValueError(msg)
        place_name_ref[name] = obj

object_name_ref = {}
monster_name_ref = {}
for (obj_name, obj) in globals().copy().items():
    if isinstance(obj, Object):
        name = obj.name
        if name in object_name_ref:     # check unique name _is_ unique
            msg = f"Object in variable '{obj_name}' doesn't have a unique identifier: '{name}'"
            raise ValueError(msg)
        object_name_ref[name] = obj

        # place Object into the required Place
        place = obj.place
        place_ref = globals()[place]
        place_ref.objects.append(name)
    elif isinstance(obj, Monster):
        name = obj.name
        if name in monster_name_ref:    # check unique name _is_ unique
            msg = f"Monster in variable '{obj_name}' doesn't have a unique identifier: '{name}'"
            raise ValueError(msg)
        monster_name_ref[name] = obj

        # place Monster into the required Place
        place = obj.place
        place_ref = place_name_ref[place]
        place_ref.monsters.append(name)

# delete globals that we no longer need that reference Place, Object and Monster instances
# not doing this confuses the "save_state()" code
del obj, place_ref

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
                    'wait': 'wait',
                   }

# the previous Place, used to implement the "short" description on revisit
previous_places = []
num_previous = 4    # the number of previous places to remember in "previous_places"

def save_state(fname):
    """Save state to the 'fname' file.

    The code first creates dictionaries of data which is saved as JSON.
    """

    # save Player, Place, Object and Monster data
    state = {'current_place': None,
             'Player': {}, 'Place': [], 'Object': [], 'Monster': []}

    for (obj_name, obj) in globals().items():
        if obj_name == 'current_place':
            state['current_place'] = obj.name
        elif isinstance(obj, Player):
            state['Player'] = obj.state()
        elif isinstance(obj, Place):
            state['Place'].append(obj.state())
        elif isinstance(obj, Object):
            state['Object'].append(obj.state())
        elif isinstance(obj, Monster):
            state['Monster'].append(obj.state())

    # save state as JSON
    with open(fname, 'w') as fd:
        fd.write(json.dumps(state, indent=4))

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
        print(f'You are {place.long_description}')
    else:
        print(f'You are {place.description}')

    # if there's an Object here, print its description
    if place.objects:
        print('\nYou see here:')
        for object_name in place.objects:
            object_ref = object_name_ref[object_name]
            print(f'\t{object_ref.description}')

    # if there are monsters here, print their descriptions
    if place.monsters:
        print('\nYou see:')
        for monster_name in place.monsters:
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

    # see if an object matching the user name is in the player's inventory
    if noun in player.inventory:
        # object there, drop it
        player.inventory.remove(noun)
        current_place.objects.append(noun)

        # update Object state
        obj_ref = object_name_ref[noun]
        obj_ref.place = current_place

        print('Dropped.')
        return

    print(f"Sorry, you aren't carrying this: {noun}.")

def pickup_object(noun):
    """If object is in 'current_place' pickup object.

    noun  the noun string the user used
    """

    # see if an object matching the user name is in the current Place
    if noun in current_place.objects:
        # object here, take it
        current_place.objects.remove(noun)
        player.inventory.append(noun)

        # update Object state
        obj_ref = object_name_ref[noun]
        obj_ref.place = None

        print('Taken.')
        return

    print(f'Sorry, I see no {noun} here.')

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
        else:
            return False
    return True

def move_monsters():
    """Move all monsters in the map."""

    # iterate over all monster references and call ".move()"
    for monster_ref in monster_name_ref.values():
        monster_ref.move()

# play the game
force_look = False
push_prev(current_place)    # start at the "current_place"

while True:
    describe_place(current_place, look=force_look)
    force_look = False
    (verb, noun) = get_command()
    if verb == 'quit':
        break
    elif verb == 'look':
        force_look = True
    else:
        if not do_command(verb, noun):
            print("Sorry, you can't do that.  Try again.\n")
    move_monsters()
    print()

save_state('state.json')

print('So long.')
