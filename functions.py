import os
import re
from termcolor import colored


def prompt():
    print(f"""Type {colored("1", "light_blue")} for deleteing parts of the filenames
Type {colored("2", "light_blue")} for changing parts of the file name
Type {colored("3", "light_blue")} for help with choosing a pattern
Type {colored("4", "light_blue")} for exiting out the application\n""")
    choice = input(colored("Please choose what you will do: ", "yellow")) 
    
    return int(choice)


def help():
    print(colored("Welcome to the help section !!!\nThis instrument supports regex patterns\nYou can use some of the patterns shown below or refer to https://cheatography.com/davechild/cheat-sheets/regular-expressions/ for further explanations\n", "green"))
    print(f"Type {colored('\\[.*?\\]', "red")} to remove or change everything in square brackets")
    print(f"Type {colored('\\{.*?\\}', "red")} to remove or change everything in curly brackets")
    print(colored("\n\nYou can also specify a pattern without the above shown regex by just typing what you want to delete or change out\n\n", "blue"))


def loopAndRename():
    directory = input("Please insert the directory here: ")
    path = f"{directory}/"
    target_pattern = input("Please enter the pattern you want to taget: ")
    result_pattern = input("Please enter what you want to change it to: ")
    try:
        # gets all directory paths, directory names and filenames in a directory tree
        for (dirpath, dirnames, filenames) in os.walk(path):
        
            #loops through every filename
            for file in filenames:

                # changes the target_pattern with result_pattern and saves it to a variable
                newfilename = re.sub(target_pattern, result_pattern, file)
            
                # uses newfilename to rename the file
                os.rename(f"{dirpath}\\{file}", f"{dirpath}\\{newfilename}")
                print(newfilename)

    except FileExistsError:
        pass


def loopAndDelete():
    directory = input("Please insert the directory here: ")
    path = f"{directory}/"
    target_pattern = input("Please enter the pattern you want to taget: ")
    try:
        # gets all directory paths, directory names and filenames in a directory tree
        for (dirpath, dirnames, filenames) in os.walk(path):
        
            #loops through every filename
            for file in filenames:

                # removes the target_pattern and saves the result to a variable
                newfilename = re.sub(target_pattern, "", file)
            
                # uses newfilename to rename the file
                os.rename(f"{dirpath}\\{file}", f"{dirpath}\\{newfilename}")
                print(newfilename)

    except FileExistsError:
        pass