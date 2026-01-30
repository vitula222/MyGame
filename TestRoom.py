import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Ещё хз")

clock = pygame.time.Clock() 
FPS = 60

wallpaper = pygame.image.load("img/Wallpaper.jpg")
button = pygame.image.load("img/Button_NotBlack.png")



class Object:
    def __init__(self, X, Y, Texture):
        self.Xy = [X, Y]
        self.Texur = pygame.image.load(Texture)
    
    def getXY(self):
        return (self.Xy[0],self.Xy[1])

    def setXY(self ,X, Y):
        self.Xy = [X, Y]
    
    def setTexture(self, Patch):
        self.Texur = pygame.image.load(Patch)
    
    def getHbox(self):
        return pygame.Rect(self.Xy[0], self.Xy[1], self.getTexur().get_width(), self.getTexur().get_height())

    
    def getTexur(self):
        return self.Texur
    
#-----обевление  обектов
Block = Object(0,700, "img/Tab.png")
Block2 = Object(600,500, "img/Tab.png")
Block3 = Object(800,-50, "img/Tab.png")

Objs = [Block, Block2, Block3]

class Player:#Player Class
    getXY = [0,100] # Корды НАшего слона
    V_run_player=0
    v0 = 0
    timeNoCal = 0
    speed = 5


    getPlayerTextura = pygame.image.load("img/player/1.jpg")

    def getHBOXV(Obj):
        Up = pygame.Rect(Player.getXY[0], Player.getXY[1], Player.getPlayerTextura.get_width(), 10)
        Down = pygame.Rect(Player.getXY[0], Player.getXY[1]+Player.getPlayerTextura.get_height(), Player.getPlayerTextura.get_width(), -10)
        if (Obj.colliderect(Down)):
            return "Down"
        if (Obj.colliderect(Up)):
            return "Up"
        return "None"
    
    def getHBOXTestDown(Obj):
        Down = pygame.Rect(Player.getXY[0], Player.getXY[1]+Player.getPlayerTextura.get_height()-10, Player.getPlayerTextura.get_width(), -20)
        if (Obj.colliderect(Down)):
            return "Down"
        return "None"
    
    def getHBOXS(Obj):
        Redy = pygame.Rect(Player.getXY[0]-10, Player.getXY[1], -10, Player.getPlayerTextura.get_height()-50)
        Left = pygame.Rect(Player.getXY[0]+Player.getPlayerTextura.get_width()+10, Player.getXY[1], -10, Player.getPlayerTextura.get_height()-50)
        if (Obj.colliderect(Left)):
            return "Left"
        if (Obj.colliderect(Redy)):
            return "Redy"
        return "None"



    def PysX(Mass):
        num=0
        for i in Objs:
            if (Player.getHBOXV(i.getHbox())=="Down"):
                num+=1  
            if (Player.getHBOXTestDown(i.getHbox())=="Down"):
                Player.getXY[1]-=5
        if (num==0):
            Player.getXY[1] += 10*Player.timeNoCal*Mass

    def jump(Mass):
        V = (Player.v0-10*Player.timeNoCal)*Mass
        Player.getXY[1] -= V
        if (V<2):
            Player.v0=0
            

ScreemWindows = 0

font = pygame.font.SysFont(None, 36)

fontN = pygame.font.SysFont(None, 90)
fontB = pygame.font.SysFont(None, 90)

LKEY = False

running = True

def exitIsGame():
    global running
    running = False
    pygame.quit()
    sys.exit()

#логика физики для обектов
def HboxLogigs():
    PlayerHBOX = pygame.Rect(Player.getXY[0], Player.getXY[1], Player.getPlayerTextura.get_width(), Player.getPlayerTextura.get_height())
    num=0
    for i in Objs:
        if (Player.getHBOXV(i.getHbox())=="Down"):
            Player.timeNoCal = 0
            if (Player.getHBOXS(i.getHbox())):
                Player.v0 = 0

            num+=1

        elif (Player.getHBOXV(i.getHbox())=="Up"):
            Player.v0 = 0
        
    if (Player.getHBOXV(i.getHbox())=="None" and num==0):
        Player.timeNoCal += 0.5


    numS=0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        for i in Objs:
            if (Player.getHBOXS(i.getHbox())=="Left"):
                numS+=1
        if (numS==0):        
            Player.getXY[0]+=Player.speed
            if keys[pygame.K_LSHIFT]:
                Player.getXY[0]+=Player.speed+2
    elif keys[pygame.K_a]:
        for i in Objs:
            if (Player.getHBOXS(i.getHbox())=="Redy"):
                print("ok")
                numS+=1
        if (numS==0):
            Player.getXY[0]-=Player.speed
            if keys[pygame.K_LSHIFT]:
                Player.getXY[0]-=Player.speed+2






class TestRoom:
    def Main():
        global ScreemWindows, LKEY, RKEY
        running = True


        while running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Выходим из цикла
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F9:
                        exitIsGame()
                    elif event.key == pygame.K_SPACE:
                        Player.v0=250
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Нажатие кнопки мыши
                    if event.button == 1:
                        LKEY = True
                    elif event.button == 3:
                        RKEY = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    # Нажатие кнопки мыши
                    if event.button == 1:
                        LKEY = False
                    elif event.button == 3:
                        RKEY = False

            

            if (ScreemWindows==0):
                screen.blit(wallpaper, (0, 0))

                screen.blit(Player.getPlayerTextura, (Player.getXY[0],Player.getXY[1]))
                
                screen.blit(Block.getTexur(), Block.getXY())
                screen.blit(Block2.getTexur(), Block2.getXY())
                screen.blit(Block3.getTexur(), Block3.getXY())

                Player.jump(0.1)
                HboxLogigs()
                Player.PysX(0.1)

            # Обновление экрана
            pygame.display.update()
            clock.tick(FPS)
            LKEY = False


        pygame.quit()