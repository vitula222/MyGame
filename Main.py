import pygame
import sys
from Setings import SetingsMenu 
import time
from TestRoom import TestRoom

pygame.init()

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Ещё хз")

clock = pygame.time.Clock()   
FPS = 60 

wallpaper = pygame.image.load("img/Wallpaper.jpg")

button = pygame.image.load("img/Button_NotBlack.png")
button2 = pygame.image.load("img/Button2.png")


logo = pygame.image.load("img/Logo.png")

WallPaperXY = [0,0,0]

ScreemWindows = 0

font = pygame.font.SysFont(None, 36)

fontN = pygame.font.SysFont(None, 90)
#fontN = pygame.font.Font("img/Text/Untitled1.sfd", 84)
fontB = pygame.font.SysFont(None, 90)

LKEY = False
RKEY = False

running = True




def exitIsGame():
    global running
    running = False
    pygame.quit()
    sys.exit()



        



class Button:

    def Button_Play():
        global RKEY, LKEY
        XY = [100, 300]
        HBOXBoutton = pygame.Rect(XY[0], XY[1], button.get_width(), button.get_height())
        name = "Играть"

        if HBOXBoutton.collidepoint(pygame.mouse.get_pos()):
            scaled_button = pygame.transform.scale(button, (button.get_width()*1.1, button.get_height()*1.1))  # в 2 раза больше
            screen.blit(scaled_button, (XY[0]-10, XY[1]-10))
            text = fontB.render(name, True, (0, 0, 0))
            screen.blit(text, (XY[0]+70, XY[1]+50))
            if (LKEY):
                TestRoom.Main()
        else:
            text = fontN.render(name, True, (0, 0, 0))
            screen.blit(button, (XY[0], XY[1]))
            screen.blit(text, (XY[0]+70, XY[1]+55))

    def Button_Setings():
        global RKEY, LKEY,ScreemWindows
        XY = [100, 500]
        name = "Настройки"
        HBOXBoutton = pygame.Rect(XY[0], XY[1], button2.get_width(), button2.get_height())
        if HBOXBoutton.collidepoint(pygame.mouse.get_pos()):
            scaled_button = pygame.transform.scale(button2, (button2.get_width()*1.1, button2.get_height()*1.1))  # в 2 раза больше
            text = fontB.render(name, True, (0, 0, 0))
            screen.blit(scaled_button, (XY[0]-10, XY[1]-10))
            screen.blit(text, (XY[0]+35, XY[1]+50))
            if (LKEY):
                ScreemWindows=1
        else:
            screen.blit(button2, (XY[0], XY[1]))

            text = fontN.render(name, True, (0, 0, 0))
            screen.blit(text, (XY[0]+30, XY[1]+50))


def ScreenLoop():
    screen.blit(wallpaper, (WallPaperXY[0], WallPaperXY[1]))

    if(WallPaperXY[2]==0):
        WallPaperXY[1] -= 1
    elif(WallPaperXY[2]==1) :
        WallPaperXY[1] +=1
    if(WallPaperXY[1]== -2400):
        WallPaperXY[2] =1
    elif(WallPaperXY[1]== 0):
        WallPaperXY[2] =0

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
                elif event.key == pygame.K_ESCAPE:
                    exitIsGame() 
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
        

        ScreenLoop()

        if (ScreemWindows==0):

            screen.blit(logo, (460, 40))
            
            Button.Button_Play()
            Button.Button_Setings()

        elif (ScreemWindows==1):
            if(SetingsMenu.Button_Back(screen, LKEY)==0):
                ScreemWindows = 0
            SetingsMenu.Button_Vol(screen, LKEY)
            SetingsMenu.Tab(screen, LKEY)
            SetingsMenu.Button_Music(screen, LKEY)



        text = font.render("Ver: 0.1", True, (0, 0, 0))
        screen.blit(text, (1825, 1048))     
        # Обновление экрана
        pygame.display.update()
        clock.tick(FPS)
        LKEY = False



    pygame.quit()
if __name__ == "__main__":
    Main()