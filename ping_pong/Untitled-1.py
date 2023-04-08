from pygame import *
import random 
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,x=0,y=0,width =65,height=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]and self.rect.y >5:
            self.rect.y -=8
        if keys[K_s] and self.rect.y<510:
            self.rect.y +=8
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]and self.rect.y >5:
            self.rect.y -=8
        if keys[K_DOWN] and self.rect.y<510:
            self.rect.y +=8


window = display.set_mode((800,600))

display.set_caption('ping_pong')
background = transform.scale(image.load('bg.png'),(800,600))
player1 = Player('platformm.png',0,210,30,90)
player2 = Player2('platformm.png',770,210,30,90)
ball = GameSprite('balls.png',200,200,50,50)
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3
finish =False
run = True
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
while run:
    for e in event.get():
        if e.type == QUIT:
            run= False
    if finish == False:
        window.blit(background,(0,0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
    
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
  
    
    if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
        speed_x *= -1
        speed_y *= 1
    if ball.rect.y >550 or ball.rect.y <0:
        speed_y *= -1
    if ball.rect.x <0:
        finish= True
        window.blit(lose1,(300,250))
        game_over = True
    if ball.rect.x > 800:
        finish = True
        window.blit(lose2,(300,250))
    display.update()
    clock.tick(FPS)
    



