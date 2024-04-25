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
            #global score_def
            #score_def += 1
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
            #global score_def
            #score_def += 1
            self.rect.y = 0
            self.rect.x = randint(0, 620)
            lost += 1
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((750, 500))
window.fill((255, 125, 125))
sprite1 = transform.scale(image.load("line.png"), (30, 110))
backgrounds = transform.scale(image.load("9370db-4.png"), (750, 500))
backgrounds_2 = transform.scale(image.load("168847-anime-anime_devushka-anime_art-multfilm-druzya_anime_braziliya-1920x1080.jpg"), (750, 500))
backgrounds_3 = transform.scale(image.load("devushka-ushki-nebo-oblaka-zdaniya-anime-8ceb3.jpg"), (750, 500))
backgrounds_4 = transform.scale(image.load("34360da60759fdd7078af0aff16b7ed1.jpg"), (750, 500))
backgrounds_mini = transform.scale(image.load("9370db-4.png"), (75, 50))
backgrounds_2_mini = transform.scale(image.load("168847-anime-anime_devushka-anime_art-multfilm-druzya_anime_braziliya-1920x1080.jpg"), (75, 50))
backgrounds_3_mini = transform.scale(image.load("devushka-ushki-nebo-oblaka-zdaniya-anime-8ceb3.jpg"), (75, 50))
backgrounds_4_mini = transform.scale(image.load("34360da60759fdd7078af0aff16b7ed1.jpg"), (75, 50))
backgrounds_mini_boom = GameSprite(backgrounds_mini, 150, 326, 0)
backgrounds_2_mini_boom = GameSprite(backgrounds_2_mini, 275, 326, 0)
backgrounds_3_mini_boom = GameSprite(backgrounds_3_mini, 400, 326, 0)
backgrounds_4_mini_boom = GameSprite(backgrounds_4_mini, 525, 326, 0)
hotcatballlol = transform.scale(image.load("—Pngtree—cute pet little wild cat_5803999 (1).png"), (100, 100))
hotcatballlol_2 = transform.scale(image.load("pngwing.com (1).png"), (100, 100))
hotcatballlol_3 = transform.scale(image.load("pngwing.com (2).png"), (100, 100))
hotcatballlol_4 = transform.scale(image.load("pngwing.com (3).png"), (100, 100))
hotcatballlol_mini = transform.scale(image.load("—Pngtree—cute pet little wild cat_5803999 (1).png"), (50, 50))
hotcatballlol_2_mini = transform.scale(image.load("pngwing.com (1).png"), (50, 50))
hotcatballlol_3_mini = transform.scale(image.load("pngwing.com (2).png"), (50, 50))
hotcatballlol_4_mini = transform.scale(image.load("pngwing.com (3).png"), (50, 50))
hotcatballlol_mini_boom = GameSprite(hotcatballlol_mini, 200, 126, 0)
hotcatballlol_2_mini_boom = GameSprite(hotcatballlol_2_mini, 300, 126, 0)
hotcatballlol_3_mini_boom = GameSprite(hotcatballlol_3_mini, 400, 126, 0)
hotcatballlol_4_mini_boom = GameSprite(hotcatballlol_4_mini, 500, 126, 0)
noob = transform.scale(image.load("NicePng_noob-saibot-png_3305375.png"), (600, 242))
accept_go_move_lets_go = transform.scale(image.load("1460084678_preview_20160408040511_1.jpg"), (178, 48))
accept = GameSprite(accept_go_move_lets_go, 286, 226, 0)
noob_gamer = GameSprite(noob, 50, 129, 0)
line1 = GameSprite(sprite1, 20, 20, 5)
line2 = GameSprite(sprite1, 700, 20, 5)
hotcat = Ball(hotcatballlol, 325, 225, 0)
hotcat_2 = Ball(hotcatballlol_2, 325, 225, 0)
hotcat_3 = Ball(hotcatballlol_3, 325, 225, 0)
hotcat_4 = Ball(hotcatballlol_4, 325, 225, 0)
game = True
back_id = 0
ball_id = 0
backgroundss = [backgrounds, backgrounds_2, backgrounds_3, backgrounds_4]
balls = [hotcat, hotcat_2, hotcat_3, hotcat_4]
lose = 1
clock = time.Clock()
while game:
    keys_pressed = key.get_pressed()
    mouse_pressed = mouse.get_pressed()
    if lose == 1:
        clock.tick(60)
        window.blit(backgroundss[back_id], (0, 0))
        accept.reset()
        backgrounds_mini_boom.reset()
        backgrounds_2_mini_boom.reset()
        backgrounds_3_mini_boom.reset()
        backgrounds_4_mini_boom.reset()
        hotcatballlol_mini_boom.reset()
        hotcatballlol_2_mini_boom.reset()
        hotcatballlol_3_mini_boom.reset()
        hotcatballlol_4_mini_boom.reset()
        display.update()
        for i in event.get():
            if i.type == MOUSEBUTTONDOWN:
                x, y = i.pos
                if x >= 276 and x <= 454 and y >= 226 and y <= 274:
                    lose = 0
                if x >= 150 and x <= 225 and y >= 326 and y <= 376:
                    back_id = 0
                if x >= 275 and x <= 350 and y >= 326 and y <= 376:
                    back_id = 1
                if x >= 400 and x <= 475 and y >= 326 and y <= 376:
                    back_id = 2
                if x >= 525 and x <= 600 and y >= 326 and y <= 376:
                    back_id = 3
                if x >= 200 and x <= 250 and y >= 126 and y <= 176:
                    ball_id = 0
                if x >= 300 and x <= 350 and y >= 126 and y <= 176:
                    ball_id = 1
                if x >= 400 and x <= 450 and y >= 126 and y <= 176:
                    ball_id = 2
                if x >= 500 and x <= 550 and y >= 126 and y <= 176:
                    ball_id = 3
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
        window.blit(backgroundss[back_id], (0, 0))

        if balls[ball_id].ud == 1:
            balls[ball_id].rect.y += 5 * cos(balls[ball_id].napr / 57.2958)
        else:
            balls[ball_id].rect.y -= 5 * cos(balls[ball_id].napr / 57.2958)
        if balls[ball_id].rl == 1:
            balls[ball_id].rect.x += 5 * sin(balls[ball_id].napr / 57.2958)
        else:
            balls[ball_id].rect.x -= 5 * sin(balls[ball_id].napr / 57.2958)

        if balls[ball_id].rect.y <= 0:
            balls[ball_id].ud *= -1
        if balls[ball_id].rect.y >= 400:
            balls[ball_id].ud *= -1
        if sprite.collide_rect(line1, balls[ball_id]) or sprite.collide_rect(line2, balls[ball_id]):
            if balls[ball_id].hotcat_touch == 0:
                balls[ball_id].rl *= -1
            balls[ball_id].hotcat_touch = 1
        else:
            balls[ball_id].hotcat_touch = 0

        for i in event.get():
            if i.type == QUIT:
                game = False
        
        line1.reset()
        line2.reset()
        balls[ball_id].update()
        display.update()
        
        if balls[ball_id].rect.x < -50 or balls[ball_id].rect.x > 700:
            lose = 1
            balls[ball_id].rect.x = 350
            balls[ball_id].rect.y = 225
            rand_napr = randint(1, 4)
            if rand_napr == 1:
                rand_napr = randint(25, 80)
            elif rand_napr == 2:
                rand_napr = randint(100, 155)
            elif rand_napr == 3:
                rand_napr = randint(205, 260)
            elif rand_napr == 4:
                rand_napr = randint(280, 335)
            balls[ball_id].napr = rand_napr
            line1.rect.x = 20
            line1.rect.y = 20
            line2.rect.x = 700
            line2.rect.y = 20
        
        #print(5 * cos(60 / 57.2958), 4 * sin(30 / 57.2958))
