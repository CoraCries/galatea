# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pygmalion")
define d = Character("Galatea")
define a = Character("Aphrodite")
define n = Character("Narrator")

# Ending Variables
default give_gift = False
default pray = False
default steal = False

#images

image bg room = ("images/bgroom.png")
image bg festival = ("images/bgfestival.png")
image bg temple = ("images/bgtemple.png")

#inventory
default inventory = []

#inventory functions
init python:
    def add_item(item):
        if item not in inventory:
                inventory.append(item)
    
    def has_item(item):
        return item in inventory

    def remove_item(item):
        if item in inventory:
            inventory.remove(item)

    #adding the pngs later
    def inventory_icon(item):
        icons = {
            "Shell": "missing.png",
            "Apple": "missing.png",
            "Cake": "missing.png",
            "Flower": "missing.png"
        }
        return icons.get(item, "missing.png")

# The game starts here.

label start:

    p "Today is the day of Aphrodite's festival."

    scene bg room

    call screen room

# Inventory Handler

label open_inventory:

    call screen inventory_screen
    $ selected_item = _return

    if selected_item:
        "You look at the [selected_item]."
    
    return

#room 1

label galatea1:
    show pygmalion at left
    p "My life's work."
    p "Her name is Galatea."
    n "Pygamalion's palm touches her out stretched hand. The ivory marble of her skin is cold as ever."
    n "He holds it gently, before releasing it and looking around the room." 

label vanity: 
    p "Motar and pestle for grinding pigment, I bought the vanity and make up for Galatea..."
    n "Sometimes he imagines her happily recieving them."

label marble: 
    n "A block of raw marble."
    p "I haven't been able to sculpt anything after her, I could never surpass her perfection."

label flowers:
    n "The roses are blooming beautifully."
    p "I thought she might like them, and when they dry I'll grind them into a paste and cook them so that she may have jewelry as lovely as her."

#Festival

label go_festival:

    scene bg festival

    call screen festival

#Beach

label shell:
    p "Oh? What's this?"
    n "Half buried in the sane, there is a luster that catches in the light of Apollo's sun."
    p "How beautiful. Perhaps the goddess will be pleased with this."

#Ending Check
label ending_check:
    if give_gift and pray and steal:
        jump morally_ambiguous
    elif give_gift and pray:
        jump happily_ever_after
    elif pray:
        jump ungrateful
    else:
        jump forever_alone

#Endings (will put stuff in later lmfao)
label morally_ambiguous:

label forever_alone:

label ungrateful:

label happily_ever_after:
    # This ends the game.

    return
