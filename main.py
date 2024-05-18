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
map_elements = []
x = 0
y=0
for i in range(1, 30):
    for j in range(1,30):
        w = Sprite(f'Ground_Tile_01_B.png', x, y, 100, 100)
        x+=50
        map_elements.append(w)
    x=0
    y+=50



def stop_game():
    global game
    game = False

btn1 = Button(535,285,stop_game, 'exit_3.png')


foodballer_1 = Sprite(img_name="allience_2.png", x=120, y=350, width=150, height=80, speed=0)
foodballer_2 = Sprite(img_name="allience.png", x=1110, y=325, width=140, height=140, speed=0)

gol_a = Sprite(img_name="Football_Goals_A.png", x=20, y=250, width=150, height=300, speed=0)
gol_b = Sprite(img_name="Football_Goals_B.png", x=1200, y=250, width=150, height=300, speed=0)
ball = Sprite(img_name="Ball.png", x=600, y=300, width=50, height=50, speed=0)

# foodball_gal= Hero(img_name="Football_Goals_A.png", x=100, y=350, width=100, height=100, speed=0)

move_direction='stop'
move_direction_2='stop'
offset_x = -500
offset_y = -500
ball_dx = -15
ball_dy = 15

while game:
    

    for e in event.get():
        if pause:
            btn1.click(e)
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pause = not pause
        if e.type == KEYDOWN:
            if e.key == K_d:
                move_direction = 'right'
            if e.key == K_a:
                move_direction = 'left'
            if e.key == K_w:
                mve_direction = 'up'
            if e.key == K_s:
                move_direction = 'down'
            if e.key == K_DOWN:
                move_direction_2 = 'down'
            if e.key == K_UP:
                move_direction_2 = 'up'
            if e.key == K_LEFT:
                move_direction_2 = 'left'
            if e.key == K_RIGHT:
                move_direction_2 = 'right'
        if e.type == KEYUP:
            if e.key == K_d:
                move_direction = 'stop'
            if e.key == K_a:
               move_direction = 'stop'
            if e.key == K_w:
                move_direction = 'stop'
            if e.key == K_s:
                move_direction = 'stop'
            if e.key == K_DOWN:
                move_direction_2 = 'stop'
            if e.key == K_RIGHT:
               move_direction_2 = 'stop'
            if e.key == K_UP:
                move_direction_2 = 'stop'
            if e.key == K_LEFT:
                move_direction_2 = 'stop'
    
    
    if move_direction == 'right':
        foodballer_1.rect.x += 15

    if move_direction == 'left':
         foodballer_1.rect.x -= 15
        
    if move_direction == 'down':
         foodballer_1.rect.y += 15
        
    if move_direction == 'up':
         foodballer_1.rect.y -= 15

         
    if move_direction_2 == 'right':
        foodballer_2.rect.x += 15

    if move_direction_2 == 'left':
         foodballer_2.rect.x -= 15
        
    if move_direction_2 == 'down':
         foodballer_2.rect.y += 15
        
    if move_direction_2 == 'up':
         foodballer_2.rect.y -= 15
            

    if pause:
        window.blit(background_pause, (0,0))
        btn1.reset(window)

        display.update()
        clock.tick(60)
        continue

    ball.rect.x += ball_dx
    ball.rect.y += ball_dy

    if ball.rect.x <=0:
        ball_dx = -ball_dx
    if ball.rect.x >= screen_width:
        ball_dx = -ball_dx

    if ball.rect.y <=0:
        ball_dy = -ball_dy
    if ball.rect.y >= screen_height:
        ball_dy = -ball_dy

    if ball.rect.colliderect(foodballer_1.rect):
        ball_dx = -ball_dx

    for i in map_elements:
        i.reset(window)
    

    foodballer_1.reset(window)
    foodballer_2.reset(window)
    gol_a.reset(window)
    gol_b.reset(window)
    ball.reset(window)
    

    display.update()
    clock.tick(120)