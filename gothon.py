# All scenes will inhereit from this class.  The enter method seems redundant?
# Do we call the enter method of the Scene class and then the enter method of the scene within that
#class?
# If  I have an instance of Death which is an instance of Scene
class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        while True:
            choice = input("Enter Command:")

        pass

class Death(Scene):

    def enter(self):
        pass
    
class CentralCorridor(Scene):

    def enter(self):
        print("You are in the central corridor of your ship.")
        pass
 
class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass
 
class EscapePod(Scene):

    def enter(self):
        pass
 
class Map(object):
    def __init__(self, start_scene):
        self.start_scene = start_scene
        pass

    def next_scene(self, scene_name):
        self.scene_name = scene_name
        pass

    def opening_scene(self):
        pass

a_map = Map('central corridor')
print(a_map.start_scene)
a_game = Engine(a_map)
a_game.play()
