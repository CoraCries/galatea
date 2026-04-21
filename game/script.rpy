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

# The game starts here.

label start:

    p "Today is the day of Aphrodite's festival."
    jump go_room1

#room 1
label go_room1:
    scene bg room
    call screen room

label galatea1:
    show pygmalion at left
    p "My life's work."
    p "Her name is Galatea."
    n "Pygmalion's palm touches her out stretched hand. The ivory marble of her skin is cold as ever."
    n "He holds it gently, before releasing it and looking around the room."

    jump go_room1

label vanity: 
    p "Motar and pestle for grinding pigment, I bought the vanity and make up for Galatea..."
    n "Sometimes he imagines her happily recieving them."
    
    jump go_room1

label marble: 
    n "A block of raw marble."
    p "I haven't been able to sculpt anything after her, I could never surpass her perfection."
    
    jump go_room1

label flowers:
    n "The roses are blooming beautifully."
    p "I thought she might like them, and when they dry I'll grind them into a paste and cook them so that she may have jewelry as lovely as her."
    menu:
        "Take a flower?"

        "Yes":
            python:
                inventory.add_item("Rose", quantity=1)
            #flavor text
        "No":
            #flavor text
    
    jump go_room1

#Festival

label go_festival:

    scene bg festival
    call screen festival

label crowd:
    n "People gather around in droves. They are dancing, chatting, and eating. There is also a man in the crowd selling apples."

    jump go_festival

label apple_vendor:
    #flavor text here

    jump go_festival

label apple_tree:
    #flavor text and mini game here
    
    jump go_festival

label beach:
    #text about going to beach
    p "Oh? What's this?"
    n "Half buried in the sane, there is a luster that catches in the light of Apollo's sun."
    p "How beautiful. Perhaps the goddess will be pleased with this."
    python:
        inventory.add_item("Shell", quantity=1)
    "Shell added to Pygmalion's inventory."
    
    jump go_festival

label home:
    #erm

#Temple

label go_temple:

    scene bg temple
    call screen temple

label aphrodite_statue:
    #flavor text

    jump go_temple

label altar:
    if pray: #no praying twice lmfao
        n "Pygmalion has already offered his prayers."
        jump go_temple

    #flavor text
    menu:
        "Pray to Aphrodite?"

        "Yes":
            $ pray = True
            #flavor text

        "No":
            #flavor text
    
    jump go_temple

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
