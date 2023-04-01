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

clock = time.Clock()
FPS = 60


finish =False
run = True
while run:
    window.blit(background,(0,0))
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    for e in event.get():
        if e.type == QUIT:
            run= False
        

    clock.tick(FPS)
    display.update()


