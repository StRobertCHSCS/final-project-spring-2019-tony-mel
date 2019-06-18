import arcade
import random
import math

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 708

class SwimmyWhale(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Swimmy Whale")
        self.upperpipe_list = None
        self.lowerpipe_list = None
        self.player_list = None

        self.player_sprite = None
        self.score = 0
        self.wallUp = arcade.Sprite("images/bottom.png")
        self.wallDown = arcade.Sprite("images/top.png")
        self.gap = 130
        self.wallx = 400
        self.birdY = 350
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False
        self.sprite = 0
        self.counter = 0

        self.offset = random.randint(-110, 110)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.upperpipe_list = arcade.SpriteList()
        self.lowerpipe_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("images/1.png")
        self.pipe_list ( 'images/pipe-green.png', 'images/pipe-red.png')

        self.score = 0

    def on_draw(self):
        arcade.start_render()
        self.upperpipe_list.draw()
        self.lowerpipe_list.draw()
        self.player_list.draw()

def main():
    """ Main method """
    window = SwimmyWhale()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()