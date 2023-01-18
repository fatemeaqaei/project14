import random
from timeit import default_timer as timer
import arcade
from spaceship import Spaceship
from enemy import Enemy
from heart import Heart

    
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=700,title="Interstellar game 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me=Spaceship(self.width)
        self.enemies = [] 
        self.hearts = []
        self.score  = 0 
        self.game_over = False
        self.last_enemy_entrance = 0.0
        self.enemy_entrance_period = 3.0
        self.inc = 0.2

        new_heart = Heart()
        self.hearts.append(new_heart)
        new_heart.center_x += 25
        new_heart1 = Heart()
        self.hearts.append(new_heart1)
        new_heart1.center_x += 55
        new_heart2 = Heart()
        self.hearts.append(new_heart2)
        new_heart2.center_x += 85

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.me.draw()
        for heart in self.heart_list:
            heart.draw()

        for enemy in self.enemy_list:
            enemy.draw()
        
        for bullet in self.me.bullet_list:
            bullet.draw()

        arcade.draw_text(self.score,self.width-50,10,arcade.color.YELLOW,20)

        if(len(self.heart_list)==0):
            arcade.draw_rectangle_filled(0,0,self.width*2,self.height*2,arcade.color.BLACK)
            # arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("Game Over!",self.width//2-50,self.height//2,arcade.color.WHITE,25)          

            a=timer()
            if(int(timer()-a)>5):
                self.enemy_list.clear()
                self.me.bullet_list.clear()
                del self.me  
                exit(0)

        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.LEFT:
            self.me.change_x=-1           
        elif symbol==arcade.key.RIGHT:
            self.me.change_x=1    
        elif symbol==arcade.key.DOWN:
            self.me.change_x=0   
        elif symbol==arcade.key.SPACE:
            self.me.fire()

    def on_update(self, delta_time: float):
        
        self.endTime=timer()
        if(self.flgStart):
            self.flgStart=0
            self.startTime=timer()      
            self.new_enemy=Enemy(self.width,self.height,self.enemySpeed)
            self.enemy_list.append(self.new_enemy)
 
        elif int(timer()-self.startTime)>=3:  
            self.startTime=timer()      
            self.new_enemy=Enemy(self.width,self.height,self.enemySpeed)
            self.enemy_list.append(self.new_enemy)

        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me,enemy):
                self.enemy_list.remove(enemy)
                for heart in self.heart_list:
                    self.heart_list.remove(heart)
                    break
                arcade.sound.play_sound(self.explosionSound)

        for bullet in self.me.bullet_list:
            for enemy in self.enemy_list:
                if arcade.check_for_collision(bullet,enemy):
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    self.score+=1
                    arcade.sound.play_sound(self.bulletSound)

        self.me.move()
        if(self.score-self.scoreOld==10):
            self.enemySpeed+=1           
            self.scoreOld=self.score

        for enemy in self.enemy_list:
            enemy.move()
            if(enemy.center_y<0):
                self.enemy_list.remove(enemy)
                for heart in self.heart_list:
                    self.heart_list.remove(heart)
                    break


        for bullet in self.me.bullet_list:
            bullet.move()
            if(bullet.center_y>self.height):
                self.me.bullet_list.remove(bullet)

window=Game()
arcade.run()