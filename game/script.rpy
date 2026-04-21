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

#Other variables
default festival_seen = False
default temple_seen = False
default flowers_seen = False

#images

image bg room = ("images/bgroom.png")
image bg festival = ("images/bgfestival.png")
image bg temple = ("images/bgtemple.png")

#inventory
default inventory = Inventory(slot_count=4, unlocked_slots=4)

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
    p "Mortar and pestle for grinding pigment, and I bought the vanity and make up for Galatea..."
    n "Sometimes he imagines her happily recieving them."
    p "...A foolish thought."
    
    jump go_room1

label marble: 
    n "A block of raw marble."
    p "I haven't been able to sculpt anything after her, I could never surpass her perfection."
    
    jump go_room1

label flowers:
    n "The roses are blooming beautifully."
    if not inventory.has_item("Rose"):
        if not flowers_seen:
            p "I thought she might like them."
            p "When they dry I'll grind them into a paste and cook them so that she may have jewelry as lovely as her."
            $ flowers_seen = True
        menu:
            "Take a flower?"

            "Yes":
                n "Pygmalion regards the roses with a thoughtful look."
                p "They're not mine to take but..."
                n "He delicately picks one up."
                p "I'm sure she would offer one to the goddess."
                python:
                    inventory.add_item("Rose", quantity=1)
                n "Pygmalion takes the rose with him."

            "No":
                n "Pygmalion shakes his head."
                p "These are for her, after all."
    
    jump go_room1

#Festival

label go_festival:

    scene bg festival

    if not festival_seen:
        n "The festival is already in full swing."
        $ festival_seen = True
    
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
    n "Pygmalion strolls along the beach."
    if not inventory.has_item("Shell"):
        p "Oh? What's this?"
        n "Half buried in the sane, there is a luster that catches in the light of Apollo's sun."
        p "How beautiful. Perhaps the goddess will be pleased with this."
        python:
            inventory.add_item("Shell", quantity=1)
        n "Pygmalion pockets the shell."
    
    jump go_festival

label home:
    #erm

#Temple

label go_temple:

    scene bg temple

    if not temple_seen:
        n "The temple is already filled with different offerings for Aphrodite."
        $ temple_seen = True

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
            n "Pygmalion bows his head and offers a heartfelt prayer to Aphrodite."
            n "He can't explain it, but he feels every word of his heard."
            $ pray = True

        "No":
            n "Pygmalion walks away from the altar without offering his prayers."
    
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
