import random
import arcade
import math
import sys

swidth = 400
sheight = 600
gravity = 1
velocity = 0
SCALE = 1



class bird(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.velocity = 0
        self.gravity = 2
        self.jump = 0
        self.jumpSpeed = 10

    def update(self):
            self.center_y -= self.gravity


class toppipes(arcade.Sprite):

    def __init__(self, filename, SCALE):
        super().__init__(filename, SCALE)
        self.pipespeed = -4


    def update(self):
        self.center_x += self.pipespeed

        # add new pipe when first pipe is about to touch left of screen
        if self.center_x < -50:
            self.center_x = 500
            self.center_y = random.randint(600, 750)

class bottompipes(arcade.Sprite):

    def __init__(self, filename, SCALE):
        super().__init__(filename, SCALE)
        self.pipespeed = -4


    def update(self):
        self.center_x += self.pipespeed

        # add new pipe when first pipe is about to touch left of screen
        if self.center_x < -50:
            self.center_x = 500
            self.center_y = random.randint(-110, 0)



class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(swidth, sheight, "Flappy bird")

        self.offset = random.randint(-110, 110)
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


        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.toppipe_list = arcade.SpriteList()
        self.bottompipe_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = bird("images/whale.png", 0.05)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 300
        self.all_sprites_list.append(self.player_sprite)

        # set up pipes
        self.toppipe_sprite = toppipes("images/top.png", SCALE)
        self.toppipe_sprite.center_x = 250
        self.toppipe_sprite.center_y = random.randint(600, 750)


        self.bottompipe_sprite = bottompipes("images/bottom.png", SCALE)
        self.bottompipe_sprite.center_x = 250
        self.bottompipe_sprite.center_y = random.randint(-110, 0)


        self.background = arcade.load_texture("images/backgroudn.jpg")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:

            self.player_sprite.center_y += 60

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.player_sprite.center_y -= 1

    def on_draw(self):
        arcade.start_render()
        # bird.draw(self)
        arcade.draw_texture_rectangle(200, 400, 0.5*self.background.width,
                                      0.5*self.background.height, self.background, 0)
        self.all_sprites_list.draw()
        self.bottompipe_sprite.draw()
        self.toppipe_sprite.draw()

        output = f" {self.score}"
        arcade.draw_text(output, swidth/2 - 30, 500, arcade.color.BLACK, 30)



    def update(self, delta_time):
        self.bottompipe_sprite.update()
        self.toppipe_sprite.update()

        self.all_sprites_list.update()

        thit = arcade.check_for_collision(self.player_sprite, self.toppipe_sprite)
        bhit = arcade.check_for_collision(self.player_sprite, self.bottompipe_sprite)

        if self.toppipe_sprite.center_x == 0:
            self.score += 1

        if thit or bhit:
            self.player_sprite.kill()
            sys.exit()


def main():
    """ Main method """
    window = MyGame()
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()
