import pygame
import sys
import json


pygame.init()

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Ещё хз")

clock = pygame.time.Clock() 
FPS = 60

wallpaper = pygame.image.load("img/Wallpaper.jpg")
button = pygame.image.load("img/Button_NotBlack.png")

wallpaperTextMenu = pygame.image.load("img/TextMenu.png")
level = 2

statusDJump = True

Smeshenie=[0,0]

Objs = []
NPCs = []
start_x = None
start_y = None

JumpOtSten = False

DialogMenu = True

class Object:
    def __init__(self, X, Y, Texture,NBT):
        self.XyN = [X, Y]
        self.Xy = [X, Y]
        self.Texur = pygame.image.load(Texture)
        self.NBT = NBT
    
    def getXY(self):
        return (self.Xy[0],self.Xy[1])

    def setXY(self ,X, Y):
        self.Xy = [self.XyN[0]+X, self.XyN[1]+Y]
    
    def setTexture(self, Patch):
        self.Texur = pygame.image.load(Patch)
    
    def getHbox(self):
        return pygame.Rect(self.Xy[0], self.Xy[1], self.getTexur().get_width(), self.getTexur().get_height())

    def getTexur(self):
        return self.Texur
    
    def getNBT(self):
        return self.NBT
    
class NPC:
    def __init__(self, X, Y, Texture,Text):
        self.XyN = [X, Y]
        self.Xy = [X, Y]
        self.Text = Text
        self.Texur = pygame.image.load(Texture)
    
    def getXY(self):
        return (self.Xy[0],self.Xy[1])

    def setXY(self ,X, Y):
        self.Xy = [self.XyN[0]+X, self.XyN[1]+Y]
    
    def setTexture(self, Patch):
        self.Texur = pygame.image.load(Patch)
    
    def getHbox(self):
        return pygame.Rect(self.Xy[0], self.Xy[1], self.getTexur().get_width(), self.getTexur().get_height())

    def getTexur(self):
        return self.Texur

    def setText(self,text):
        self.Text = text
    
    def getText(self):
        return self.Text

def get_level(level_name):
    global start_x, start_y,Objs,NPCs
    Objs = []
    NPCs = []
    with open(level_name, "r", encoding="utf-8") as f:
        level = json.load(f)

    start_x = level["start_position"][0]
    start_y = level["start_position"][1]

    for i in level["objects"].values():
        Objs.append(Object(i["cords"][0]+940, i["cords"][1]+540, i["texture"],i["NBT"]))

    if level["npcs"] != None:
        for i in level["npcs"].values():
            NPCs.append(NPC(i["cords"][0]+940, i["cords"][1]+540, i["texture"],i["text"]))

get_level(f"levels/level{level}.json")

class Player:#Player Class
    getXY = [start_x,start_y] # Корды НАшего слона
    center = [940,540]
    V_run_player=0
    v0 = 0
    timeNoCal = 0
    speed = 5


    getPlayerTextura = pygame.image.load("img/player/stoitP.png")

    def getHBOXV(Obj):
        Up = pygame.Rect(Player.center[0], Player.center[1], Player.getPlayerTextura.get_width(), 10)
        Down = pygame.Rect(Player.center[0], Player.center[1]+Player.getPlayerTextura.get_height(), Player.getPlayerTextura.get_width(), -10)
        if (Obj.colliderect(Down)):
            return "Down"
        if (Obj.colliderect(Up)):
            return "Up"
        return "None"
    
    def getHBOXTestDown(Obj):
        Down = pygame.Rect(Player.center[0],Player.center[1]+Player.getPlayerTextura.get_height()-10, Player.getPlayerTextura.get_width(), -20)
        if (Obj.colliderect(Down)):
            return "Down"
        return "None"
    
    def getHBOXS(Obj):
        Redy = pygame.Rect(Player.center[0], Player.center[1], 10, Player.getPlayerTextura.get_height()-50)
        Left = pygame.Rect(Player.center[0]+Player.getPlayerTextura.get_width()+10, Player.center[1], -10, Player.getPlayerTextura.get_height()-50)
        if (Obj.colliderect(Left)):
            return "Left"
        if (Obj.colliderect(Redy)):
            return "Redy"
        return "None"

    def setTexur(name):
        Player.getPlayerTextura = pygame.image.load("img/player/"+name)

    def PysX(Mass):
        num=0
        for i in Objs:
            if (Player.getHBOXV(i.getHbox())=="Down"):
                num+=1  
            if (Player.getHBOXTestDown(i.getHbox())=="Down"):
                Player.getXY[1] -= 1
        if (num==0):
            Player.getXY[1] += 10*Player.timeNoCal*Mass

    def jump(Mass):
        V = (Player.v0-10*Player.timeNoCal)*Mass
        Player.getXY[1] -= V
        if (V<2):
            Player.v0=0
            

def Camera():
    Smeshenie[0] = Player.getXY[0]
    Smeshenie[1] = Player.getXY[1]

    print(Smeshenie)

    for i in Objs:
        i.setXY(-Smeshenie[0], -Smeshenie[1])

    for i in NPCs:
        i.setXY(-Smeshenie[0], -Smeshenie[1])

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
    global level,Objs,NPCs
    num=0
    for i in Objs:
        if (Player.getHBOXV(i.getHbox())=="Down"):
            #------------------тут условия для NBT
            if (i.getNBT()=="kill"):
                Player.getXY = [start_x,start_y]

            if (i.getNBT()=="next"):
                level += 1
                get_level(f"levels/level{str(level)}.json")


            Player.timeNoCal = 0
            num+=1

        if (Player.getHBOXS(i.getHbox())=="Left"):
            if (JumpOtSten and statusDJump):
                Player.setTexur("Left_up.png")
                Player.timeNoCal = 0
                Player.v0 = 200

        elif (Player.getHBOXS(i.getHbox())=="Redy"):
            if (JumpOtSten and statusDJump):
                Player.setTexur("Read_up.png")
                Player.timeNoCal = 0
                Player.v0 = 200
            

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
            Player.setTexur("go_left.png")
    elif keys[pygame.K_a]:
        for i in Objs:
            if (Player.getHBOXS(i.getHbox())=="Redy"):
                numS+=1
        if (numS==0):
            Player.getXY[0]-=Player.speed
            if keys[pygame.K_LSHIFT]:
                Player.getXY[0]-=Player.speed+2
            Player.setTexur("go_Read.png")
    else:
        Player.setTexur("stoitP.png")






class TestRoom:
    def Main():
        global ScreemWindows, LKEY, Objs,JumpOtSten,wallpaperTextMenu

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
                        JumpOtSten =True
                        Player.v0 = 200
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        JumpOtSten = False
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




            screen.blit(wallpaper, (0-Smeshenie[0], 0-Smeshenie[1]))
    
            screen.blit(Player.getPlayerTextura, (960,540))

            for i in Objs:
                screen.blit(i.getTexur(), i.getXY())

            for i in NPCs:
                screen.blit(i.getTexur(), i.getXY())
                if (Player.getHBOXS(i.getHbox())!="None"):
                    screen.blit(wallpaperTextMenu,(520,830))
                    strS = i.getText().split("\n")
                    ints = 0
                    for a in strS:
                        text = font.render(a, True, (255, 255, 255))
                        screen.blit(text, (530, 840+20*ints)) 
                        ints+=1

            Player.jump(0.1)
            Player.PysX(0.1)
            Camera()
            HboxLogigs()
            # Обновление экрана
            pygame.display.update()
            clock.tick(FPS)
            LKEY = False


        pygame.quit()