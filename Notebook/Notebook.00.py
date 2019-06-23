"""
Notebook.00.py

Usage: Notebook.00.py <notebook_file>

Commands: help
          quit
          delete <title>
          dir
"""

import sys
import json

def get_cmd():
    """Get command, return as list, first element lowercase."""

    while True:
        ans = input('> ')
        ans = ans.strip()
        if ans:
            result = ans.split()
            result[0] = result[0].lower()
            return result

def pause():
    input('Press ENTER to continue ')

def usage(msg=None):
    """Print usage text with optional message."""

    if msg:
        print('*' * 60)
        print(msg)
        print('*' * 60)
    print(__doc__)

def bad_cmd(cmd):
    """Describe bad command."""

    print(f"Bad command: {' '.join(cmd)}\n")

def bad_title(title):
    """Describe error: no such title."""

    print(f"No such title: '{title}'\n")

def notebook(notebook_path):
    """Handle simple commands in a notebook."""

    # open input notebook and get JSON dictionary
    try:
        with open(notebook_path) as fd:
            notebook = json.loads(fd.read())
    except FileNotFoundError:
        usage(f"File '{notebook_path}' not found.")
        sys.exit(1)

    while True:
        # get command string
        cmd = get_cmd()
        if ('|' + cmd[0]) in '|quit':
            return
        if cmd[0] == 'help':
            usage()
        elif cmd[0] == 'dir':
            for (key, value) in notebook.items():
                print(f'{key:20s} {value}')
            print()
        elif cmd[0] in ['del', 'delete']:
            # must have a second argument, the title
            if len(cmd) != 2:
                bad_cmd(cmd)
                continue
            title = cmd[1]
            try:
                del notebook[title]
            except KeyError:
                bad_title(title)
        else:
            bad_cmd(cmd)

# get the input and output filenames and the text message
if len(sys.argv) != 2:
    usage('Sorry, expected a notebook file')
    sys.exit(1)

notebook_path = sys.argv[1]

notebook(notebook_path)


