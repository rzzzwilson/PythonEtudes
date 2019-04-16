"""
Experimental "curses-lite" code from:
https://solarianprogrammer.com/2019/04/08/c-programming-ansi-escape-codes-windows-macos-linux-terminals/
"""

import sys
from time import sleep
from enum import Enum, auto

ESC = ''

class Colors(Enum):
	RESET_COLOR = 1
	BLACK_TXT = 30
	RED_TXT = 31
	GREEN_TXT = auto()
	YELLOW_TXT = auto()
	BLUE_TXT = auto()
	MAGENTA_TXT = auto()
	CYAN_TXT = auto()
	WHITE_TXT = auto()

	BLACK_BKG = 40,
	RED_BKG = auto()
	GREEN_BKG = auto()
	YELLOW_BKG = auto()
	BLUE_BKG = auto()
	MAGENTA_BKG = auto()
	CYAN_BKG = auto()
	WHITE_BKG = auto()

class ClearCodes(Enum):
	CLEAR_FROM_CURSOR_TO_END = 1
	CLEAR_FROM_CURSOR_TO_BEGIN = 2
	CLEAR_ALL = 3


def log(msg):
    with open('test.log', 'a') as f:
        f.write(msg + '\n')

def log_init():
    with open('test.log', 'w') as f:
        pass


def setTextColor(color):
    log(f'Printing: ESC [ {color.value} ;1m')
    print(f'{ESC}[{color.value};1m', end='')
    sys.stdout.flush()

def clearScreen():
    print(f'{ESC}[{ClearCodes.CLEAR_ALL.value}J', end='')
    sys.stdout.flush()

def clearScreenToBottom():
    print(f'{ESC}[{ClearCodes.CLEAR_FROM_CURSOR_TO_END.value}J', end='')
    sys.stdout.flush()

def clearScreenToTop():
    print(f'{ESC}[{ClearCodes.CLEAR_FROM_CURSOR_TO_BEGIN.value}J', end='')
    sys.stdout.flush()

def clearLine():
    print(f'{ESC}[{ClearCodes.CLEAR_ALL.value}K', end='')
    sys.stdout.flush()

def clearLineToRight():
    print(f'{ESC}[{ClearCodes.CLEAR_FROM_CURSOR_TO_END.value}K', end='')
    sys.stdout.flush()

def clearLineToLeft():
    print(f'{ESC}[{ClearCodes.CLEAR_FROM_CURSOR_TO_BEGIN.value}K', end='')
    sys.stdout.flush()

def moveUp(positions):
    print(f'{ESC}[{positions}A', end='')
    sys.stdout.flush()
 
def moveDown(positions):
    print(f'{ESC}[{positions}B', end='')
    sys.stdout.flush()
 
def moveRight(positions):
    print(f'{ESC}[{positions}C', end='');
    sys.stdout.flush()
 
def moveLeft(positions):
    print(f'{ESC}[{positions}D', end='');
    sys.stdout.flush()
 
def moveTo(row, col):
    print(f'{ESC}[{row};{col}f', end='');
    sys.stdout.flush()
 
def restoreConsole():
    print(f'{ESC}[0m')

#print(f'{ESC}[32mHello, World')
#print(f'{ESC}[31m{ESC}[44mHello, World')
#print(f'{ESC}[0m', end='')

def main():
#    setupConsole()
    
    setTextColor(Colors.GREEN_TXT)
    setTextColor(Colors.YELLOW_BKG)

    clearScreen()

    moveTo(1,1)
    print("Text line 1")
    print("Text line 2")
    print("Text line 3")

    moveUp(2)

    clearLine()
    print("Replacement for second line")

    moveDown(3)
    moveRight(5)

    setTextColor(Colors.MAGENTA_TXT)
    print("5 positions to right ...")

    moveTo(15, 40)
    print('Sleeping for 10 seconds...')
    sleep(10)

    restoreConsole()
    clearScreenToBottom()
    sleep(3)
    clearScreen()

log_init()
main()
