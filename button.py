from pygame import *

class Button:
    def __init__(self, window, screen_width, screen_height):
        self.window = window
        self.width = 100
        self.height = 50
        self.x = screen_width/2
        self.y = screen_height/2

        font.init()
        self.font1 = font.Font(None, 20)

    def reset(self): 
        draw.rect(self.window, (255,255,255), rect.Rect( self.x,  self.y,  self.width,  self.height))
        self.window.blit(self.font1.render('Exit', True, (0,0,0)),(self.x,  self.y,))

    def click(self):
        mouse1 = mouse.get_pos()
        if mouse1[0] >= self.x and mouse1[0] <= self.x + self.width and mouse1[1] >= self.y and mouse1[1] <= self.y + self.height:
            print(mouse1)


