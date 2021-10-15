# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define anemo = Character ("Anemo Slime(s)")
define h = Character ("Harry")
define c = Character ("Crewmate")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    show mango 

    show crewmate

    python:
            name = renpy.input("Enter your name")
            name = name.strip() or "Default Joe"

    c "sussy"

    c "yoooooo what's up [name]"

    menu:
        
        "Yes, let's play Among Us":
            jump agree
        
        "No, let's play Cookie Clicker":
            jump diagree

    label agree:
        $ importantdecisionagree = True
        c "Yay!"

    return

    label disagree:
        $ importantdecisionagree = False
        c "No you sussy baka"

    return

