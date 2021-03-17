"""
Code for spawning walls
"""
import arcade


class Wall():
        def __init__(self):
            self.wall_list = None
            self.texture = None
            self.platform_layer_name = ''
            self.center_x = 0
            self.center_y = 0
        
        def setup(self):
            # TODO: write code that all walls can derive from to draw, and manipulate with exceptions
            # Unbreakable walls:
            StaleWalls = StaleCracker()
            StaleWalls.setup
            StaleWalls.draw
            # Breakable walls:

class StaleCracker(Wall):
        def __init__(self):
                super().__init__()
                # TODO: set unique dimensions! (center_x&y = ?)
                self.texture = arcade.Sprite("assets/milkboy/PLACEHOLDER_walls.jpg")
                self.plaform_layer_name = 'stale_cracker'
                
        """
        Load specifics of a StaleCracker wall, remember they are smaller and can't break
        """
        def setup(self):
            self.coordinate_list = [[512, 96],
                           [256, 96],
                           [768, 96]]
            self.draw()
            
        def draw(self):
            for coordinate in self.coordinate_list:
                instance = arcade.Sprite(self.texture)
                instance.texture.position = coordinate
                Wall.wall_list.append(instance)
    
class BreakableCracker(Wall):
        def __init__(self):
                super().__init__()
                # TODO: set unique dimensions! (center_x&y = ?)
                pass