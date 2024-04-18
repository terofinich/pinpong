from pygame import *
from random import *
from math import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = player_image
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def fire(self):
        global bullets
        global bullet_png
        bullet = Bullet(bullet_png, self.rect.centerx, self.rect.top, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            global score_def
            score_def += 1
            self.rect.y = 0
            self.rect.x = randint(0, 620)
            lost += 1
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        napr = 0
        ud = 1
        rl = 1
        rand_napr = randint(1, 4)
        if rand_napr == 1:
            rand_napr = randint(25, 80)
        elif rand_napr == 2:
            rand_napr = randint(100, 155)
        elif rand_napr == 3:
            rand_napr = randint(205, 260)
        elif rand_napr == 4:
            rand_napr = randint(280, 335)
        self.napr = rand_napr
        self.ud = 1
        self.rl = 1
        self.hotcat_touch = 0
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            global score_def
            score_def += 1
            self.rect.y = 0
            self.rect.x = randint(0, 620)
            lost += 1
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((750, 500))
window.fill((255, 125, 125))
sprite1 = transform.scale(image.load("line.png"), (30, 110))
backgrounds = transform.scale(image.load("9370db-4.png"), (750, 500))
hotcatballlol = transform.scale(image.load("—Pngtree—cute pet little wild cat_5803999 (1).png"), (100, 100))
noob = transform.scale(image.load("NicePng_noob-saibot-png_3305375.png"), (600, 242))
accept_go_move_lets_go = transform.scale(image.load("1460084678_preview_20160408040511_1.jpg"), (178, 48))
accept = GameSprite(accept_go_move_lets_go, 276, 226, 0)
noob_gamer = GameSprite(noob, 50, 129, 0)
line1 = GameSprite(sprite1, 20, 20, 5)
line2 = GameSprite(sprite1, 700, 20, 5)
hotcat = Ball(hotcatballlol, 350, 225, 0)
game = True
lose = 1
clock = time.Clock()
while game:
    keys_pressed = key.get_pressed()
    mouse_pressed = mouse.get_pressed()
    if lose == 1:
        clock.tick(60)
        window.blit(backgrounds, (0, 0))
        accept.reset()
        display.update()
        for i in event.get():
            if i.type == MOUSEBUTTONDOWN:
                x, y = i.pos
                if x >= 276 and x <= 454 and y >= 226 and y <= 274:
                    lose = 0
            if i.type == QUIT:
                game = False
    else:
        if keys_pressed[K_w] and line1.rect.y > 0:
            line1.rect.y -= line1.speed
        if keys_pressed[K_s] and line1.rect.y < 390:
            line1.rect.y += line1.speed
        if keys_pressed[K_UP] and line2.rect.y > 0:
            line2.rect.y -= line2.speed
        if keys_pressed[K_DOWN] and line2.rect.y < 390:
            line2.rect.y += line2.speed
        clock.tick(60)
        window.blit(backgrounds, (0, 0))
        
        if hotcat.ud == 1:
            hotcat.rect.y += 5 * cos(hotcat.napr / 57.2958)
        else:
            hotcat.rect.y -= 5 * cos(hotcat.napr / 57.2958)
        if hotcat.rl == 1:
            hotcat.rect.x += 5 * sin(hotcat.napr / 57.2958)
        else:
            hotcat.rect.x -= 5 * sin(hotcat.napr / 57.2958)

        if hotcat.rect.y <= 0:
            hotcat.ud *= -1
        if hotcat.rect.y >= 400:
            hotcat.ud *= -1
        if sprite.collide_rect(line1, hotcat) or sprite.collide_rect(line2, hotcat):
            if hotcat.hotcat_touch == 0:
                hotcat.rl *= -1
            hotcat.hotcat_touch = 1
        else:
            hotcat.hotcat_touch = 0

        for i in event.get():
            if i.type == QUIT:
                game = False
        
        line1.reset()
        line2.reset()
        hotcat.update()
        display.update()
        
        if hotcat.rect.x < -100 or hotcat.rect.x > 700:
            lose = 1
            hotcat.rect.x = 350
            hotcat.rect.y = 225
            rand_napr = randint(1, 4)
            if rand_napr == 1:
                rand_napr = randint(25, 80)
            elif rand_napr == 2:
                rand_napr = randint(100, 155)
            elif rand_napr == 3:
                rand_napr = randint(205, 260)
            elif rand_napr == 4:
                rand_napr = randint(280, 335)
            hotcat.napr = rand_napr
            line1.rect.x = 20
            line1.rect.y = 20
            line2.rect.x = 700
            line2.rect.y = 20
        
        #print(5 * cos(60 / 57.2958), 4 * sin(30 / 57.2958))
