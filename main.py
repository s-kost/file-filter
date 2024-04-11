from functions import *
from art import *
import sys
from termcolor import colored

print(colored(welcome, "green"))
print(colored("This instrument is used for manipulating filenames\nUse it to either change or delete reoccuring parts of filenames\n", "green"))

while True:
    try:
        match prompt():
            case 1:
                loopAndDelete()
            case 2:
                loopAndRename()
            case 3:
                help()
            case 4:
                print(colored("Thank you for using my script!! :)", "magenta"))
                sys.exit()
            case _:
                print(colored("Please provide a valid value", "red"))
    except ValueError:
        print(colored("Please provide a valid value", "red"))
