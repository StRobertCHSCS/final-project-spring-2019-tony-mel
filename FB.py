import random
import arcade
import math

swidth = 400
sheight = 600
gravity = 1
velocity = 0
SCALE = 1


class bird(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.y = swidth / 2
        self.x = 25
        self.velocity = 0
        self.gravity = 1

    def update(self):
        self.center_x += 0

class pipes(arcade.Sprite):

    def __init__(self, filename, SCALE):
        super().__init__(filename, SCALE)
        self.size = 0
        self.pipespeed = -1

    def update(self):

        self.center_x += self.pipespeed

        if self.center_x == -50:
            self.center_x += 500








class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(swidth, sheight, "Flappy bird")

        self.offset = random.randint(-110, 110)
        self.wallx = 400
        self.frame_count = 0

        self.game_over = False


        self.all_sprites_list = None
        self.toppipe_list = None
        self.bottompipe_list = None
        self.toppipe_sprite = None
        self.bottompipe_sprite = None

        # Set up the player
        self.score = 0
        self.player_sprite = None



        self.set_mouse_visible(False)

    def start_new_game(self):
        self.frame_count = 0
        self.game_over = False

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.toppipe_list = arcade.SpriteList()
        self.bottompipe_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = bird("images/bird1.png", SCALE)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 300
        self.all_sprites_list.append(self.player_sprite)
        self.lives = 3

        #set up pipes
        self.toppipe_sprite = pipes("images/top.png", SCALE)
        self.toppipe_sprite.center_x = 250
        self.toppipe_sprite.center_y = 600
        self.all_sprites_list.append(self.toppipe_sprite)

        self.bottompipe_sprite = pipes("images/bottom.png", SCALE)
        self.bottompipe_sprite.center_x = 250
        self.bottompipe_sprite.center_y = 0
        self.all_sprites_list.append(self.bottompipe_sprite)



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
        self.all_sprites_list.draw()


    def update(self, delta_time):
        self.all_sprites_list.update()








def main():
    """ Main method """
    window = MyGame()
    window.start_new_game()
    arcade.run()

if __name__ == "__main__":
    main()