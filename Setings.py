import pygame
import yaml
import time


pygame.init()

wallpaper = pygame.image.load("img/Wallpaper.jpg")

button = pygame.image.load("img/Smail_Button.png")
button2 = pygame.image.load("img/Button2.png")

tab = pygame.image.load("img/Tab.png")

fontN = pygame.font.SysFont(None, 90)
fontB = pygame.font.SysFont(None, 90)

def Edit_File(String):
    with open('config.yaml', 'w') as file:
        yaml.dump(String, file, default_flow_style=False)
def Read_File():
    with open('config.yaml') as f:
        return yaml.safe_load(f)

class SetingsMenu:
    def Tab(screen, LKEY):
        screen.blit(tab, (600, 30))



    def Button_Back(screen, LKEY):
        XY = [50, 50]
        HBOXBoutton = pygame.Rect(XY[0], XY[1], button.get_width(), button.get_height())
        name = "<-"

        if HBOXBoutton.collidepoint(pygame.mouse.get_pos()):
            scaled_button = pygame.transform.scale(button, (button.get_width()*1.1, button.get_height()*1.1))  # в 2 раза больше
            screen.blit(scaled_button, (XY[0]-10, XY[1]-10))
            text = fontB.render(name, True, (0, 0, 0))
            screen.blit(text, (XY[0]+30, XY[1]+20))
            if (LKEY):
                return 0
        else:
            text = fontN.render(name, True, (0, 0, 0))
            screen.blit(button, (XY[0], XY[1]))
            screen.blit(text, (XY[0]+20, XY[1]+20))
            return
    def Button_Vol(screen, LKEY):
        i = Read_File()['Vol']['All_music']

        XY = [100, 250]
        HBOXBoutton = pygame.Rect(XY[0], XY[1], button2.get_width(), button2.get_height())
        name = "Val: " + str(i)

        if HBOXBoutton.collidepoint(pygame.mouse.get_pos()):
            scaled_button = pygame.transform.scale(button2, (button2.get_width()*1.1, button2.get_height()*1.1))  # в 2 раза больше
            screen.blit(scaled_button, (XY[0]-10, XY[1]-10))
            text = fontB.render(name, True, (0, 0, 0))
            screen.blit(text, (XY[0]+70, XY[1]+50))
            if (LKEY):
                scaled_button = pygame.transform.scale(button2, (button2.get_width()*1.2, button2.get_height()*1.2))  # в 2 раза больше
                screen.blit(scaled_button, (XY[0]-10, XY[1]-10))
                text = fontB.render(name, True, (0, 0, 0))
                screen.blit(text, (XY[0]+80, XY[1]+60))
                if(int(i)<10):
                    i+=1
                else:
                    i=0
                date = {
                    "Vol":{
                        "All_music": i,
                        "Music": Read_File()['Vol']['Music']

                    }
                }
                Edit_File(date)

                return
        else:
            text = fontN.render(name, True, (0, 0, 0))
            screen.blit(button2, (XY[0], XY[1]))
            screen.blit(text, (XY[0]+70, XY[1]+55))
            return
        
    def Button_Music(screen, LKEY):
        i = Read_File()['Vol']['Music']

        XY = [100, 450]
        HBOXBoutton = pygame.Rect(XY[0], XY[1], button2.get_width(), button2.get_height())
        name = "Music: " + str(i)

        if HBOXBoutton.collidepoint(pygame.mouse.get_pos()):
            scaled_button = pygame.transform.scale(button2, (button2.get_width()*1.1, button2.get_height()*1.1))  # в 2 раза больше
            screen.blit(scaled_button, (XY[0]-10, XY[1]-10))
            text = fontB.render(name, True, (0, 0, 0))
            screen.blit(text, (XY[0]+50, XY[1]+50))
            if (LKEY):
                scaled_button = pygame.transform.scale(button2, (button2.get_width()*1.2, button2.get_height()*1.2))  # в 2 раза больше
                screen.blit(scaled_button, (XY[0]-10, XY[1]-10))
                text = fontB.render(name, True, (0, 0, 0))
                screen.blit(text, (XY[0]+60, XY[1]+60))

                i = not i
                date = {
                    "Vol":{
                        "All_music": Read_File()['Vol']['All_music'],
                        "Music": i
                    }
                }
                Edit_File(date)

                return
        else:
            text = fontN.render(name, True, (0, 0, 0))
            screen.blit(button2, (XY[0], XY[1]))
            screen.blit(text, (XY[0]+50, XY[1]+55))
            return
            
