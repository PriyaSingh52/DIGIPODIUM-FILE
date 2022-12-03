import pgzrun

HEIGHT = 500
WIDTH = 800

p = Actor('ironman', (100,100))
e1 = Actor('ennemy01', (700, 400))

def draw():  
    screen.fill("black")
    p.draw()
    e1.draw()
  
def update():
    print(p.pos, e1.pos)
    # player control
    if keyboard.left: 
       p.x -= 5
       p.angle = 10
       sounds.bomb.play()
    elif keyboard.right:
        p.x += 5
        p.angle = -10
        sounds.arrow.play()
    elif keyboard.up:
        p.y -= 5
    elif keyboard.down:
        p.y += 5
    elif keyboard.SPACE:
        p.angle = 180   
    else:
        p.angle = 0  


    # enemy control
    if p.x > e1.x:
        e1.x += 1
    if p.y > e1.y:
        e1.y += 1
    if p.x < e1.x:
        e1.x -= 1  
    if p.y < e1.y:
        e1.y -= 1                
pgzrun.go()
