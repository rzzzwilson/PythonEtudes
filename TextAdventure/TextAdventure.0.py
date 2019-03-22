"""
This experimental code is trying to implement a simple text adventure.

We just have static data structures describing places.  The player may
move around with the usual commands.

Some features:

* "textual" linkages between Places to fix the "forward reference" problem
* code to print short descriptions of a place if visited recently

"""

class Place:
    """A Place in the text adventure."""

    def __init__(self, name, description, connections):
        self.name = name
        self.description = description
        self.connections = connections

    def __str__(self):
        """For debug."""

        return f"Place('{self.name}')"


# the Places in this adventure
white_house = Place('white_house', 'at the White house.',
                    connections = {'east': 'path',
                                   'south': 'forest'})

path = Place('path', 'on a narrow path.',
             connections={'east': 'glade',
                          'west': 'white_house'})

glade = Place('glade', 'in a shadowed glade.',
              connections = {'west': 'path',
                             'southwest': 'forest'})

forest = Place('forest', 'in a dark difficult forest.',
               connections={'northeast': 'glade',
                            'north': 'white_house'})

# a dictionary to map place "names" to the actual Place() object
# solves the "forward reference" problem
# this definition must come AFTER all Places are defined
name_place = {'white_house': white_house,
              'path': path,
              'glade': glade,
              'forest': forest
             }

current_place = white_house

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
    """

    print('You are ' + place.description)

def get_move():
    """Get a legal move command.
   
    Accepts any of the canonical moves even if it won't work
    in the current Place.

    Returns the canonical direction string.
    """

    while True:
        move = input('Which way? ').lower()
        try:
            return allowed_moves[move]
        except KeyError:
            print(f"Sorry, '{move}' isn't a legal move here.  Try again.\n")

def make_move(move):
    """Check if the move is legal in the current Place.  If so, move there.

    move  the canonical move string

    Returns True if move OK and "current_place" is updated.
    Returns False if move not allowed.
    """

    global current_place

    if move in current_place.connections:
        current_place = name_place[current_place.connections[move]]
        return True
    return False


# play the game
while True:
    describe_place(current_place)
    move = get_move()
    if not make_move(move):
        print("Sorry, you can't move in that direction.  Try again.\n")
