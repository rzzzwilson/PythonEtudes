class Place:
    def __init__(self, name, description, long_description=None,
                 connections=None, things_here=None):
        self.name = name
        self.description = description
        if long_description is None:
            long_description = description
        self.long_description = long_description
        if connections is None:
            connections = {}
        self.connections = connections
        if things_here is None:
            things_here = []
        self.things_here = things_here

    def __str__(self):
        return f"Place('{self.name}')"

white_house = Place('white_house', 'at the White house.',
                    'at the White house, a decaying white weatherboard house.  '
                    'There are paths to the east and south.',
                    connections = {'east': 'path',
                                   'south': 'forest'})
path = Place('path', 'on a narrow path.',
             'on a narrow path.  The path runs east-west.',
             connections={'east': 'glade',
                          'west': 'white_house'})
glade = Place('glade', 'in a shadowed glade.',
              'in a shadowed glade, with exits to the west and southwest.',
              connections = {'west': 'path',
                             'southwest': 'forest'})
forest = Place('forest', 'in a dark difficult forest.',
               'in a dark difficult forest, with paths leading north and northeast.',
        connections={'northeast': 'glade',
                     'north': 'white_house'})

# a dictionary to map place "names" to the actual Place() object
# solves the "forward reference" problem
name_place = {'white_house': white_house,
              'path': path,
              'glade': glade,
              'forest': forest
             }

current_place = white_house
previous_place = None

allowed_moves = {'north': 'north', 'n': 'north',
                 'northeast': 'northeast', 'ne': 'northeast',
                 'east': 'east', 'e': 'east',
                 'southeast': 'southeast', 'se': 'southeast',
                 'south': 'south', 's': 'south',
                 'southwest': 'southwest', 'sw': 'southwest',
                 'west': 'west', 'w': 'west',
                 'northwest': 'northwest', 'nw': 'northwest',
                }

def describe_place(place):
    """Describe the current place.
    
    place  a reference to the Place() object to describe

    If we have just come from this place, print a short description.
    """

    if place != previous_place:
        print('You are ' + place.long_description)
    else:
        print('You are ' + place.description)


def get_move():
    """Get a legal move command.
    
    Returns the canonical direction string.
    """

    while True:
        move = input('Which way? ').lower()
        if move in allowed_moves:
            return allowed_moves[move]
        print(f"Sorry, '{move}' isn't a legal move here.  Try again.\n")

def allow_move(move):
    """Check if the move is legal.  If so, move there.

    move  the canonical move string

    Returns True if move OK and "current_place" is updated.
    Returns False if move not allowed.
    """

    global current_place
    global previous_place

    if move in current_place.connections:
        new_place = name_place[current_place.connections[move]]
        describe_place(new_place)
        (previous_place, current_place) = (current_place, new_place)
        return True
    return False


# play the game
describe_place(current_place)
while True:
    move = get_move()
    if not allow_move(move):
        print("Sorry, that isn't a legal move here.  Try again.\n")
