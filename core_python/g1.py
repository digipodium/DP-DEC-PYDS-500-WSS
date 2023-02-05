import pgzrun

WIDTH = 640
box = Rect((50,50), (100,100)) 
box2 = Rect((150,150), (130,30))

def draw():
    screen.fill('white') # White background
    screen.draw.filled_rect(box, 'red') # Red box
    screen.draw.filled_rect(box2, 'blue') # Blue box

def update():
    if box.x > WIDTH:
        box.x = 0
    box.x += 3
    

pgzrun.go()