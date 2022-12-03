import pgzrun

from game_controls import HEIGHT

WIDTH = 1200
HIGHT = 500

p = Actor('ironman', (100,100)) # player
p.speed = 5

rx = random.randint(50, WIDTH-50)
ry = random.randint(50,HEIGHT-50)
c = Actor('cookie_img', (rx, ry))  #cookie

score = 0

def draw():
    if score <= 10:
       screen.clear()
       p.draw()
       c.draw()
       screen.draw.text(f'Score : {score}', (WIDTH-120,10), fontsize=30)
       screen.draw.text(f'WASD to move' , (10,10), fontsize=30)
    else:
        screen.fill('green')
        screen.draw.text(f'You Win!', (WIDTH/2-100, HEIGHT/2-50), fontsize=50)


def player_control():  
    if keyboard.W:
        p.y -= p.speed
    elif keyboard.S:
        p.y += p.speed 
    elif keyboard.A:
        p.y += p.speed 
        p.angle = 10
    elif keyboard.D:
        p.y += p.speed 
        p.angle = -10
    else:
        p.angle = 0

    # boundary
    if p.x < 0:
        p.x = WIDTH
    if p.x < 0:
        p.x = 0
            

           

def handle_score():
    global score
    if p.colliderect(c):
        rx = random.randint(50, WIDTH-50)
        ry = random.randint(50 ,HEIGHT-50)
        c.pos = (rx,ry)
        score += 1

def update():
    player_control()
    handle_score()

pgzrun.go()