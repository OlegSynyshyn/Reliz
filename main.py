from pygame import *
from button import Button
from sprites import *
init()

info = display.Info() 
screen_width,screen_height = info.current_w,info.current_h

window = display.set_mode((screen_width,screen_height))
background = transform.scale(image.load('bg.jpg'),(screen_width,screen_height) )
background_pause = transform.scale(image.load('pause.jpg'),(screen_width,screen_height) )
game = True
pause = False

clock = time.Clock()

btn1 = Button(window, screen_width,screen_height)

treasure1 = Sprite(img_name="treasures.png", x = 250, y = 250)
rover = Sprite()
hero = Hero()


while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pause = not pause
        if e.type == MOUSEBUTTONDOWN:
            btn1.click()

    if pause:
        
        window.blit(background_pause, (0,0))
        btn1.reset()

        display.update()
        clock.tick(60)
        continue

    window.blit(background, (0,0))
    
    treasure1.reset(window)
    rover.reset(window)
    hero.reset(window)

    display.update()
    clock.tick(60)