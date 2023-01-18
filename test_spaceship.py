import random
import arcade


class Spaceship(arcade.Sprite):
    def __init__(self, w, name):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = w // 2
        self.center_y = 80
        self.width = 48
        self.height = 48
        #self.name = name
        self.speed = 8


class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, w)
        self.center_y = h + 24
        self.angle = 180
        self.width = 48
        self.height = 48


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=800, title="Insterstellar Game 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self.width, "Fateme")
        self.doshman = Enemy(self.width, self.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        self.doshman.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        #print("one key pressed")
        # print(symbol)

        if symbol == arcade.key.LEFT:
            self.me.center_x = self.me.center_x - self.me.speed
        if symbol == arcade.key.RIGHT:
            self.me.center_x = self.me.center_x + self.me.speed
        elif symbol == arcade.key.SPACE:
            ...

    def on_update(self, delta_time: float):
        self.doshman.center_y -= self.doshman.speed


window = Game()
arcade.run()
