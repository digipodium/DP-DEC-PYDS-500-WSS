import pgzrun
from random import randint as r
WIDTH = 800
HEIGHT = 500
box_red = Rect((10,10), (20, 100))
box_blue = Rect((WIDTH-30, 10), (20, 100))
balls = []
ball = Rect((WIDTH/2, HEIGHT/2), (20, 20))
brs, bbs, bs = 5, 6, (r(1,10), r(-10,10))

def draw():
    screen.fill('white')
    screen.draw.filled_rect(box_red, 'red')
    screen.draw.filled_rect(box_blue, 'blue')
    for b in balls:
        screen.draw.filled_rect(b, 'black')

def update():
    global brs, bbs, bs
    brs = move_vertically(box_red, brs) # call
    bbs = move_vertically(box_blue, bbs) # call
    # print(box_red.bottom, box_red.top, box_red.y, brs)
    for b in balls:
        bs = move_ball(b, bs)

# defination
def move_vertically(box, speed):
    box.y += speed
    if box.bottom >= HEIGHT or box.top <= 0:
        speed = -speed
    return speed

def move_ball(b, s):
    b.x += s[0]
    b.y += s[1]
    if b.bottom >= HEIGHT or b.top <= 0:
        s = s[0], -s[1]
    if b.left <= 0 or b.right >= WIDTH:
        s = -s[0], s[1]
    # collision
    if b.colliderect(box_red) or b.colliderect(box_blue):
        s = -s[0], s[1]
    return s
pgzrun.go()