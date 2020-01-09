from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print("Abcd")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print("\n--------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    quips = [
        "You died. You kind a suck at this.",
        "Your mom would be proud",
        "such a luser",
        "i have a puppy"
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("gothan invaded your ship")

        action = raw_input("> ")

        if action == "shoot!":
            print("quick onthe draw")
            return "death"
        elif action == "dodge!":
            print("you dodged")
            return "death"
        elif action == "tell a joke":
            print("lucky for you")
            return "laser_weapon_armory"
        else:
            print("DOES NOT COMPUTE")
            return "central_corridor"

class Laser_Weapon_Armory(Scene):
    def enter(self):
        print("You do a dive roll")
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZEEDDDD")
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print("The container clicks open")
            return "the_bridge"
        else:
            print("The lock buzzes one last time")
            return "death"


class The_Bridge(Scene):
    def enter(self):
        print("You burst onto the bridge with the nuetron destruct bomb")

        action = raw_input("> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb")
            return "death"
        elif action == "slowly place the bomb":
            print("You point you blaster at the bomb under your arm")
        else:
            print("DOES NOT COMPUTE")
            return "the_bridge"
            

class Escape_pod(Scene):
    def enter(self):
        print("You rush through the ship desperetly trying to make it to")
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button.") %guess
            return "death"
        else:
            print("You jump into pod %s and hit the eject button.") %guess
            return "finished"

class Map(object):
    scenes = {
        'central_corridor' : CentralCorridor(),
        'death' : Death()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        Val = Map.scenes.get(scene_name)
        return Val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
        
    