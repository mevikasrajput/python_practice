from sys import exit

def gold_room():
    print("This room is full of gold,how much do you take?")

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("man, learn to write numbers")
    if how_much < 50:
        print("nice, you're not greedy,you win.")
        exit(0)
    else:
        dead("you greedy bastard.")

def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat")
    print("how are you going")
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("the bear loks at you")
        elif next == "taunt bear" and not bear_moved:
            print("the bear is moved from the door")
            bear_moved = True
        elif next == "tant bear" and bear_moved:
            dead("the bear gets pissed off and chews your leg off")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means")

def chthulu_room():
    print("here you see")
    print("you go insane")
    print("do you fle?")

    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty")
    else:
        chthulu_room()

def dead(why):
    print(why,"good job!")
    exit(0)

def start():
    print("you're in a dark room")
    print("there's a door to your left n your right")
    print("which one do you take?")

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        chthulu_room()
    else:
        dead("you stumble")

start()

