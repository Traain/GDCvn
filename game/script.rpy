# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define anemo = Character ("Anemo Slime(s)")
define h = Character ("Harry")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    show mango 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show anemoslime happy

    # These display lines of dialogue.

    anemo "You've created a new Ren'Py game."

    anemo "Once you add a story, pictures, and music, you can release it to the world!"

    show anemoslime group
    # This ends the game.

    anemo "Now we are a group"

  

    return
