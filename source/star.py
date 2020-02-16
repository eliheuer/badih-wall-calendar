from drawBot import *

def star(x, y, n, r1, r2):
    pts = []
    for i in range(n * 2):
        a = i * pi / n
        r = r2 if i % 2 else r1
        pts.append((x + r * sin(a), y + r * cos(a)))
    polygon(*pts)

fill(1,0,0)
star(500, 500, 19, 450, 160)

saveImage("star.gif")
