"""
An initial attemp the the "Two Jugs" problem:

https://ps.reddit.com/r/learnpython/comments/9y54oz/trying_to_create_create_code_you_have_2_jugs_of/

That is, given a jug of size 4 gallons, another jug of size 3 gallons, how can
you measure 2 gallons in the 4 gallon jug?

The idea is to do Depth-First Search (DFS) and have a list as a queue of states,
initially populated with the start state.  We have a loop that pops a state off
the list, calculates the various new states from the set of possible operations
and pushes those new states to the right end of the list.  Continue until we
have a state matching the desired state.

Initially, use jugs of 4 and 3 gallons (or litres, doesn't matter) and expand
later to allow changeable jug sizes and the required amount in whatever
jug.

The "state" is a tuple (A, B) of two integers, the first for jug A, etc.
"""

import sys


MaxJugA = 4
MaxJugB = 3
InitState = (0, 0)  # the initial state: both jugs empty
DesiredAState = 2

######
# Functions: given a state, manipulate the jug state and return the new state.
######

def empty_jug_a(state):
#    print(f'empty_jug_a: state={state}')
    return (0, state[1])

def empty_jug_b(state):
#    print(f'empty_jug_b: state={state}')
    return (state[0], 0)

def fill_jug_a(state):
#    print(f'fill_jug_a: state={state}')
    return (MaxJugA, state[1])

def fill_jug_b(state):
#    print(f'fill_jug_b: state={state}')
    return (state[0], MaxJugB)

def fill_jug_a_from_b(state):
#    print(f'fill_jug_a_from_b: state={state}')
    a_vol = state[0]
    b_vol = state[1]
    a_empty = MaxJugA - a_vol
    if b_vol > a_empty:
        # A goes full, B still has something
        a_vol = MaxJugA
        b_vol -= a_empty
    else:
        # B goes empty, A is fuller but maybe not full
        a_vol += b_vol
        b_vol = 0
    return (a_vol, b_vol)

def fill_jug_b_from_a(state):
#    print(f'fill_jug_b_from_a: state={state}')
    a_vol = state[0]
    b_vol = state[1]
    b_empty = MaxJugB - b_vol
    if a_vol > b_empty:
        # B goes full, A still has something
        b_vol = MaxJugB
        a_vol -= b_empty
    else:
        # A goes empty, B is fuller but maybe not full
        b_vol += a_vol
        a_vol = 0
    return (a_vol, b_vol)

# list of possible operations on jugs
operations = [empty_jug_a, empty_jug_b,
              fill_jug_a, fill_jug_b,
              fill_jug_a_from_b, fill_jug_b_from_a]

######
# Main code.  Implement a Breadth-first Search.  We use BFS because we
# want the shortest solution.  Use a list as a "pending states" queue.
######

pending_states = [(0, 0)]
seen_states = [[(0, 0)]]
soln_length = None

while True:
#    print(f'loop: pending_states={pending_states}, seen_states={seen_states}')
    state = pending_states.pop(0)
    seen = seen_states.pop(0)
    for op in operations:
        new_state = op(state)
        if new_state[0] == DesiredAState:
            if soln_length is None:
                soln_length = len(seen)
            if len(seen) > soln_length:
                sys.exit(0)
            print(f'Solution: {seen+[new_state]}')
        if new_state not in pending_states:
            pending_states.append(new_state)
            seen_states.append(seen+[new_state])

