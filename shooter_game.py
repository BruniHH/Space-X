#Создай собственный Шутер!

from pygame import *
from random import randint

bul = 3
score = 0
#Спрайты 
window = display.set_mode((700, 500))
display.set_caption("SpaceWAR")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

bullet_points = 3

font.init()
font = font.Font(None, 39)
welcome = font.render("Welcome, to start press q!", True, (255, 215, 0))
reload_bullets = font.render("Bullets:" + str(bul), True, (255, 215, 0))






mixer.init()
mixer.music.load('fire.ogg')

class Rocket(sprite.Sprite):
    def __init__(self, r_image, r_x, r_y, r_speed):
        super().__init__()
        self.image = transform.scale(image.load(r_image), (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = r_x
        self.rect.y = r_y
        self.speed = r_speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def right(self):
        self.rect.x += self.speed
    def left(self):
        self.rect.x -= self.speed
    def up(self):
        self.rect.y -= self.speed
    def down(self):
        self.rect.y += self.speed
    def win_move(self):
        self.rect.y -= 7

class Bullet(sprite.Sprite):
    def __init__(self, b_image, b_x, b_y, b_speed):
        super().__init__()
        self.b_image = transform.scale(image.load(b_image), (35, 35))
        self.rect = self.b_image.get_rect()
        self.rect.x = b_x
        self.rect.y = b_y
        self.speed = b_speed
    def draw_bullet(self):
        window.blit(self.b_image, (self.rect.x, self.rect.y))
    def shot(self):
        self.rect.y -= self.speed
    def hide_b(self):
        self.rect.x = 10000000
        self.rect.y = 10000000

class Enemy(sprite.Sprite):
    def __init__(self, e_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(e_image), (100, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def go_down(self):
        self.rect.y += self.speed
    def hide(self):
        self.rect.x = 100000000
        self.rect.y = 100000000
class Asteroid(Enemy):
    def __init__(self, image, x, y):
        super().__init__()
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameOver(sprite.Sprite):
    def __init__(self, image_astr, x, y):
        super().__init__()
        self.load = transform.scale(image.load(image_astr), (1000, 10))
        self.rect = self.load.get_rect()
        self.rect.x = x
        self.rect.y = y
    def appear(self):
        window.blit(self.load, (self.rect.x, self.rect.y))

class Heart(sprite.Sprite):
    def __init__(self, image_heart, x, y):
        super().__init__()
        self.load = transform.scale(image.load(image_heart), (60, 60))
        self.rect = self.load.get_rect()
        self.rect.x = x
        self.rect.y = y
    def appear(self):
        window.blit(self.load, (self.rect.x, self.rect.y))
    def hide(self):
        self.rect.x = 100000000
        self.rect.y = 100000000

spisok = ["ufo.png", "asteroid.png"]


rocket = Rocket("rocket.png", 300, 400, 4)
asteroid1 = GameOver("asteroid.png", 0, -100)




bullets = []
enemies = []
k = 0
count = 0
bullet_count = 0
hearts = []
heart_point = 3
u = 1




h2 = Heart("heart.png", 0, 380)

wait1 = 0
#ФПС

clock = time.Clock()
fps = 60

game = True
go = False
space = 0
wait = 0

while game:
    clock.tick(fps)
    key_pressed = key.get_pressed()

    key_press = key.get_pressed()
    window.blit(background, (0, 0))
    window.blit(welcome, (0,0))
    window.blit(reload_bullets, (0,450))



        



    if key_press[K_q]:
        welcome = font.render("Score:" + str(score), True, (255, 215, 0))
        window.blit(welcome, (0,0))
        go = True
    
    rocket.draw()
    asteroid1.appear()
    h2.appear()

    
    if go == True:
        if key_pressed[K_d] and rocket.rect.x < 600:
            rocket.right()
        if key_pressed[K_a] and rocket.rect.x > 5:
            rocket.left()

        if key_pressed[K_e] and count != 1 and bullet_count != 3:
            bullet = Bullet("bullet.png", rocket.rect.x + 35, rocket.rect.y, 4)
            bullets.append(bullet)
            count = 1
            bullet_count += 1
            bul -= 1
            reload_bullets = font.render("Bullets:" +str(bul), True, (255, 215, 0))
            window.blit(reload_bullets, (0,450))

            mixer.music.load('fire.ogg')
            mixer.music.play()
        if not key_pressed[K_e]:
            count = 0
        if bullet_count == 3:
            if wait1 == 0:
                wait1 = 20
                reload_bullets = font.render("Reloading...(Press R)", True, (255, 215, 0))
                window.blit(reload_bullets, (0,450))
                bul = 3
                if key_pressed[K_r]:
                    bullet_count = 0
                    reload_bullets = font.render("Bullets:" +str(bul), True, (255, 215, 0))
                    window.blit(reload_bullets, (0,450))
            wait1 -= 1
        
        for i in bullets:
            i.draw_bullet()
            i.shot()

        
        if wait == 0:
            wait = 60
            if len(enemies) != 5:
                p =  spisok[randint(0,1)]
                enemy = Enemy(p, randint(1, 600), 0, randint(1, 1))
                enemies.append(enemy)
      
        wait -= 1
        
        for enemy in enemies:
            enemy.show()
            enemy.go_down()

            if enemy.rect.y > 500:
                h2.hide()
                enemy.hide()
                u -= 1

            if sprite.collide_rect(rocket, enemy):
                enemy.hide()
                h2.hide()
                u -= 1
            
            
            
                
            
                

            for i1 in bullets:
                if sprite.collide_rect(i1, enemy):
                    enemy.hide()
                    i1.hide_b()
                    bullets.remove(i1)
                    enemies.remove(enemy)
                    score += 1
                    welcome = font.render("Score:" + str(score), True, (255, 215, 0))
        if score == 10:
            win = font.render("YOU WIN!!!!!!", True, (255, 215, 0))
            window.blit(win, (350, 250))
            for i2 in enemies:
                i2.rect.x = 100000
                i2.rect.y = -100
            rocket.win_move()
        if sprite.collide_rect(rocket, asteroid1):
            h2.hide()
            u -= 1
        
        if u == -100:
            game = False
            

            
    display.update()
    for e in event.get():
        if e.type == QUIT:
            game = False

