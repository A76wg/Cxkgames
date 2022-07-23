import pygame,sys
import easygui
from random import randint
from easygui import buttonbox
from easygui import msgbox
import time

from pygame.locals import *
pygame.init()
pygame.mixer.init()

bg=pygame.image.load('img/flfbg0.3plus.bmp')
flfimg=pygame.image.load('img/kun222.png')
xhimg=pygame.image.load('img/xhimage.png')
life1=pygame.image.load('img/life1 2.2.bmp')
life2=pygame.image.load('img/life2 2.2.bmp')
life3=pygame.image.load('img/life3 2.2.bmp')
gameoverbg=pygame.image.load('img/gameoversp.bmp')
startbg=pygame.image.load('img/start.bmp')



canvas=pygame.display.set_mode((1600,800))
canvas.fill((255,255,255))
pygame.display.set_caption("逃离菜虚坤")

def refresh():
    pygame.display.update()
    
def fillText(text, position,size):
    # 设置字体
    TextFont = pygame.font.Font('ft/SIMHEI.TTF', size)
    # 设置字体其他样式
    newText = TextFont.render(text, True, (0, 0, 0))
    canvas.blit(newText, position)  

def game():
    point=0
    user_x=int(easygui.enterbox('请输入出生点on x'))
    user_y=int(easygui.enterbox('请输入出生点on y'))
    life=3
    while True:
        flf_x=randint(0,1474)
        flf_y=randint(0,704)
        canvas.blit(bg,(0,0))
        canvas.blit(flfimg,(flf_x,flf_y))
        canvas.blit(xhimg,(user_x,user_y))
        refresh()
        print(point)
        for event in pygame.event.get():
            if event.type==QUIT:
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key==ord('w'):
                    user_y-=10
                if event.key==K_a:
                    user_x-=10
                if event.key==K_s:
                    user_y+=10
                if event.key==K_d:
                    user_x+=10
                if event.key==K_q:
                    user_x-=5
                    user_y-=5
                if event.key==K_e:
                    user_x+=5
                    user_y-=5
                if event.key==K_z:
                    user_x-=5
                    user_y+=5
                if event.key==K_c:
                    user_x+=5
                    user_y+=5
                if event.key==K_h:
                    pass
                if event.key==K_r:
                    again()
                if event.key==K_n and event.key==K_m and event.key==K_l:
                    canvas.blit(akm,(800,400))
                if event.key==(K_ESCAPE or K_o):
                    print('SCORE',str(int(point)))
                    pygame.quit()
                    sys.exit()
                #sound
                pygame.mixer.music.load('mus/jntm.mp3')
                pygame.mixer.music.play()
        if life==3:
            canvas.blit(life3,(5,5))
            refresh()
        elif life==2:
            canvas.blit(life2,(5,5))
            refresh()
        elif life==1:
            canvas.blit(life1,(5,5))
            refresh()
        if (user_x==flf_x) or (user_y==flf_y):
            life-=1
        else:
            pass
        if life<=0:
            canvas.blit(gameoverbg,(0,0))
            fillText('你被鲲鲲抓住了，得分：'+str(int(point)),(30,5),35)
            refresh()
            print('SCORE:  '+str(int(point)))
            pygame.mixer.music.load('mus/jntm2.mp3')
            pygame.mixer.music.play()
            time.sleep(5)
            sys.exit()
        if life>0 and user_x>1475 and user_y>705:
            canvas.blit(gameoverbg,(0,0))
            fillText('你成功逃出了鲲鲲，得分：'+str(int(point)),(30,5),35)
            pygame.mixer.music.load('mus/jntm2.mp3')
            pygame.mixer.music.play()
            time.sleep(5)
            sys.exit()
        if user_x<0:
            user_x=1
        if user_x>1600:
            user_x=1500
        if user_y<55:
            user_y=56
        if user_y>800:
            user_y=700
        point+=0.001
        

def startInBg():
    while True:
        canvas.blit(startbg,(0,0))
        refresh()
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_i:
                    game()
                    
                    

def again():
    game()
    
startInBg()
game()
