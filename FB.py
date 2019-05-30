import random
import arcade
import math

swidth = 400
sheight = 600
gravity = 1
velocity = 0


class bird(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.y = swidth / 2
        self.x = 25
        self.velocity = 0
        self.gravity = 1

    def update(self):
        self. velocity += gravity
        self.y += self.velocity

        if self.y > sheight:
            self.y = sheight
            self.velocity = 0


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(swidth, sheight, "Flappy bird")

        self.offset = random.randint(-110, 110)
        self.wallx = 400



        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    #def setup(self):

    def updateWalls(self):
        self.wallx -= 2
        if self.wallx < -80:
            self.wallx = 400
            self.counter += 1
            self.offset = random.randint(-110, 110)




    def on_draw(self):
        arcade.start_render()
        #bird.draw(self)


        arcade.draw_circle_filled(25, 200, 16, arcade.color.WHITE_SMOKE)








def main():
    """ Main method """
    window = MyGame()
    arcade.run()
    bird.update(60)




if __name__ == "__main__":
    main()