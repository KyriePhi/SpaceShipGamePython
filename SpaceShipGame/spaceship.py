# Design/Program : Mehmet Berat Şenel ( mehmetberat.com )
import pygame
import random

pygame.init()

my_font = pygame.font.SysFont('Arial Bold', 30)

gameDisplay = pygame.display.set_mode((1280,720))
pygame.display.set_caption('SpaceShip (beta v1)')
programIcon = pygame.image.load('.icon/spaceship.png')
width = gameDisplay.get_width()
height = gameDisplay.get_height()

pygame.display.set_icon(programIcon)

clock = pygame.time.Clock()

crashed = False
shipa=pygame.image.load('.img/ship1.png')
shipb=pygame.image.load('.img/ship2.png')
monstera=pygame.image.load('.img/monstera.png')
monsterb=pygame.image.load('.img/monsterb.png')
bg=pygame.image.load('.img/background.png')
blltimg=pygame.image.load('.img/lazer.png')
mainbg=pygame.image.load(".img/mainbg.png")
overbg=pygame.image.load(".img/overbg.png")

LaserSound=pygame.mixer.Sound(".sound/laser.wav")
GameMusic=pygame.mixer.Sound(".sound/Kubbi - Digestive biscuit.wav")
MainMusic=pygame.mixer.Sound(".sound/c152 - Night Mission.wav")
BombSound=pygame.mixer.Sound(".sound/Bomb.wav")
CreditMusic=pygame.mixer.Sound(".sound/man-is-he-mega-glbml-22045.wav")

lightlist=list()
bullets=list()
monsters=list()
shipx=10
shipy=300
counter=0
up=False
down=False
left=False
right_=False
score=0
play=2
GameMusicPlay=0
MainMusicPlay=0
CreditMusicPlay=0
level=0
speed=-4

def GameOver():
    global GameMusicPlay,MainMusicPlay,CreditMusicPlay,play,crashed
    if CreditMusicPlay==0:
        GameMusicPlay=0
        MainMusicPlay=0
        CreditMusicPlay=1
        pygame.mixer.stop()
        pygame.mixer.Sound.play(CreditMusic)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
              if 550 <= mouse[0] <= 730 and 600 <= mouse[1] <= 620:
                play=2
    gameDisplay.blit(overbg,(0,0))
    my_font = pygame.font.SysFont('Arial Bold', 70)
    text_surface = my_font.render('Score : '+str(score), True, (178, 238, 0))
    text_surface1 = my_font.render('Level  : '+str(level), True, (178, 238, 0))
    my_font1 = pygame.font.SysFont('Arial Bold', 30)
    text_surface6 = my_font1.render('< BACK TO MENU >', True, (178, 238, 0))
    gameDisplay.blit(text_surface, (500,10+300))
    gameDisplay.blit(text_surface1, (500,100+300))
    gameDisplay.blit(text_surface6, (550,300+300))

def credit():
    global GameMusicPlay,MainMusicPlay,CreditMusicPlay,play,crashed
    if CreditMusicPlay==0:
        GameMusicPlay=0
        MainMusicPlay=0
        CreditMusicPlay=1
        pygame.mixer.stop()
        pygame.mixer.Sound.play(CreditMusic)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
              if 550 <= mouse[0] <= 730 and 600 <= mouse[1] <= 620:
                play=2
    gameDisplay.fill((22,22,22))
    text_surface = my_font.render('Programmer / Game Designer', True, (178, 238, 0))
    text_surface1 = my_font.render('* Mehmet Berat ŞENEL ( mehmetberat.com )', True, (178, 238, 0))
    text_surface2 = my_font.render('Sounds', True, (178, 238, 0))
    text_surface3 = my_font.render('* c152 - Night Mission Synthwave', True, (178, 238, 0))
    text_surface4 = my_font.render('* Kubbi - Digestive biscuit', True, (178, 238, 0))
    text_surface5 = my_font.render('* Man is He Mega - GLBML by GeoffreyBurch', True, (178, 238, 0))
    text_surface6 = my_font.render('< BACK TO MENU >', True, (178, 238, 0))
    gameDisplay.blit(text_surface, (400,10+200))
    gameDisplay.blit(text_surface1, (450,60+200))
    gameDisplay.blit(text_surface2, (400,110+200))
    gameDisplay.blit(text_surface3, (450,160+200))
    gameDisplay.blit(text_surface4, (450,210+200))
    gameDisplay.blit(text_surface5, (450,260+200))
    gameDisplay.blit(text_surface6, (550,300+300))
    
def MainMenu():
    global GameMusicPlay,MainMusicPlay,my_font,play,mainbg,CreditMusicPlay,crashed,lightlist,bullets,monsters,shipx,shipy,counter,score,level,speed,up,down,left,right_
    lightlist=list()
    bullets=list()
    monsters=list()
    shipx=10
    shipy=300
    counter=0
    score=0
    level=0
    speed=-4
    up=False
    down=False
    left=False
    right_=False
    if MainMusicPlay==0:
        GameMusicPlay=0
        MainMusicPlay=1
        CreditMusicPlay=0
        pygame.mixer.stop()
        pygame.mixer.Sound.play(MainMusic)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
              if width/2-90 <= mouse[0] <= width/2+50 and height/2-50 <= mouse[1] <= height/2+30:
                play=0
        if event.type == pygame.MOUSEBUTTONDOWN:
              if width/2-150 <= mouse[0] <= width/2+120 and height/2+50 <= mouse[1] <= height/2+100:
                play=1
    gameDisplay.fill((0,0,0))
    gameDisplay.blit(mainbg,(0,0))

def Game():
    global crashed,up,down,left,right_,GameMusicPlay,MainMusicPlay,CreditMusicPlay
    if GameMusicPlay==0:
        GameMusicPlay=1
        MainMusicPlay=0
        CreditMusicPlay=0
        pygame.mixer.stop()
        pygame.mixer.Sound.play(GameMusic)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up=True
            elif event.key == pygame.K_LEFT:
                left=True
            elif event.key == pygame.K_DOWN:
                down=True
            elif event.key == pygame.K_RIGHT:
                right_=True
            elif event.key== pygame.K_x:
                if level>=5:
                    bullets.append((shipx+68,shipy+15))
                    bullets.append((shipx+68,shipy+70))
                else:
                    bullets.append((shipx+68,shipy+40))
                pygame.mixer.Sound.play(LaserSound)
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_UP:
                up=False
            elif event.key == pygame.K_LEFT:
                left=False
            elif event.key == pygame.K_DOWN:
                down=False
            elif event.key == pygame.K_RIGHT:
                right_=False

    gameDisplay.fill((0,0,0))
    BGControl()
    ship(shipx,shipy)
    Mnstrcrt()
    bullet()
    text_surface = my_font.render('Score : '+str(score), True, (178, 238, 0))
    text_surface1 = my_font.render('Level : '+str(level), True, (178, 238, 0))
    gameDisplay.blit(text_surface, (10,10))
    gameDisplay.blit(text_surface1, (10,50))



def BGCreater():
    rdcount=1
    for i in range(rdcount):
        rdx=random.randint(1,10000)
        rdy=random.randint(1,720)
        lightlist.append((rdx+1280,rdy))

def BGControl():
    for i in range(len(lightlist)):
        gameDisplay.blit(bg,lightlist[i])
        lightlist[i]=(lightlist[i][0]-3,lightlist[i][1])
    BGCreater()

def bullet():
    global speed,score
    for i in range(len(bullets)):
        try:
            gameDisplay.blit(blltimg,bullets[i])
            bullets[i]=(bullets[i][0]+10+level,bullets[i][1])
            for cords in monsters:
                if bullets[i][1] in list(range(cords[1],cords[1]+100)) and cords[0]<bullets[i][0]:
                    pygame.mixer.Sound.play(BombSound)
                    bullets.remove(bullets[i])
                    monsters.remove(cords)
                    score+=level
                    speed=-level*0.5-3
        except:
            pass
        

def monster(x,y):
    global counter,speed
    if counter<4:
        gameDisplay.blit(monstera,(x,y))
    else:
        gameDisplay.blit(monsterb,(x,y))

def Mnstrcrt():
    global play
    MonsterControl()
    for i in range(len(monsters)):
        if monsters[i][0]<0:
            play=3
        monster(monsters[i][0],monsters[i][1])
        monsters[i]=(monsters[i][0]+speed,monsters[i][1])

def MonsterControl():
    global level
    if len(monsters)==0:
        level+=1
        for i in range(random.randint(level+2,level+5)):
            monsters.append((random.randint(10,500)+1280,random.randint(20,700)))
                

def ship(x,y):
    global counter,up,down,left,right_,shipx,shipy
    if counter<4:
        gameDisplay.blit(shipa,(x,y))
        counter+=1
    elif counter==9:
        gameDisplay.blit(shipb,(x,y))
        counter=0
    else:
        gameDisplay.blit(shipb,(x,y))
        counter+=1
    if up:
        shipy-=level+5
    if down:
        shipy+=level+5
    if left:
        shipx-=level+5
    if right_:
        shipx+=level+5

while not crashed:

    if play==0:
        Game()
    elif play==1:
        credit()
    elif play==2:
        MainMenu()
    else:
        GameOver()

    pygame.display.update()
    clock.tick(60)
