import random
import arcade
import math
import sys

swidth = 400
sheight = 600
gravity = 1
velocity = 0
SCALE = 1
gap  = 100 # gap between upper and lower part of pipe
basey = sheight* 0.79
hitmasks = {}



class bird(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.velocity = 0
        self.gravity = 1
        self.jump = 0
        self.jumpSpeed = 10

    def update(self):
        self.center_y -= self.gravity
        #if self.jump:
            #self.jumpSpeed -= 1
            #self.y -= self.jumpSpeed
            #self.jump -= 1
        #else:
            #self.y += self.gravity
            #self.gravity += 0.2


class pipes(arcade.Sprite):

    def __init__(self, filename, SCALE):
        super().__init__(filename, SCALE)
        self.size = 0
        self.pipespeed = -4

    def update(self):
        self.center_x += self.pipespeed

            # add new pipe when first pipe is about to touch left of screen
        if 0 < self.center_x < 5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

            # remove first pipe if its out of the screen
        if upperPipes[0]['x'] < -IMAGES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)








        self.center_x += self.pipespeed

        if self.center_x == -50:
            self.center_x += 500

        if self.center_x == 500:
            self.center_y











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
        self.player_sprite = bird("images/spiderman.png", 0.05)
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




        arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

    #def setup(self):

    def updateWalls(self):
        self.wallx -= 2
        if self.wallx < -80:
            self.wallx = 400
            self.counter += 1
            self.offset = random.randint(-110, 110)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.player_sprite.center_y +=30




    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.player_sprite.center_y -= 1

    def on_draw(self):
        arcade.start_render()
        #bird.draw(self)
        self.all_sprites_list.draw()


    def update(self, delta_time):
        self.all_sprites_list.update()

        thit = arcade.check_for_collision(self.player_sprite, self.toppipe_sprite)
        bhit = arcade.check_for_collision(self.player_sprite, self.bottompipe_sprite)

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