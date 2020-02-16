# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com

from drawBot import *
import math

# [W]IDTH, [H]EIGHT, [M]ARGIN, [F]FONT-SIZE
# Note: 1 inch = 72 units
W,H,M,F = 612,792,54,72
CENTER = M+(F*3.5)

# GRID
def grid():
    stroke(0.9)
    strokeWidth(1)
    lineCap("round")
    stepX, stepY = 0, 0
    incX, incY = 72, 72
    for x in range(8):
        polygon(((M)+stepX, M),
                ((M)+stepX, (H-(F*2))-(M+((F/4)*2))))
        stepX += incX
    for y in range(8):
        polygon((M, (M)+stepY),
                (W-(M), (M)+stepY))
        stepY += incY

def star(x, y, n, r1, r2):
    pts = []
    for i in range(n * 2):
        a = i * pi / n
        r = r2 if i % 2 else r1
        pts.append((x + r * sin(a), y + r * cos(a)))
    polygon(*pts)

# NEW PAGE
def new_page():
    newPage(W, H)

# MAIN
new_page()
#grid() # Toggle for grid view
stroke(None)

# Draw calendar
fill(None)
stroke(0)
oval(CENTER-2, CENTER-2, 4, 4)
oval(M,M,F*7,F*7)
oval(M+(F/2),M+(F/2),F*6,F*6)

star(CENTER, CENTER, 19, 252, 0)
fill(1)
oval(M+(F*2.5),M+(F*2.5),F*2,F*2)
#star(CENTER, CENTER, 5, F, F/2.75)

#amp = F/2
#step = 0
#x_pos = CENTER
#y_pos = CENTER
#stroke(1,0,0)
#for i in range(29):
#    polygon((CENTER, CENTER), (x_pos, y_pos))
#    x_pos += cos(step) * amp
#    y_pos += -1 * sin(step) * amp
#    print("x_pos =", x_pos)
#    print("y_pos =", y_pos)
#    step += 0.2
#    stroke(0)

stroke(None)
fill(0)
fontSize(F*2.3)
font("fonts/Amiri-Bold.ttf")
text("ملك", (M*7.8, M*11), align="right")
fontSize(F)
text("١", (M*5.35, M*5.4), align="right")
text("٧٦", (M*6.75, M*5.4), align="right")
fontSize(F/3)


text("١", (325, 385), align="right")
text("٢", (355, 375), align="right")
text("٣", (375, 357), align="right")
text("٤", (388, 335), align="right")
text("٥", (394, 308), align="right")
text("٦", (394, 280), align="right")
text("٧", (385, 253), align="right")
text("٨", (365, 235), align="right")
text("٩", (340, 220), align="right")
tracking(-5)
text("١٠", (313, 215), align="right")
text("١١", (285, 218), align="right")
text("١٢", (260, 230), align="right")
text("١٣", (240, 250), align="right")
text("١٤", (230, 280), align="right")
text("١٥", (225, 308), align="right")
text("١٦", (230, 336), align="right")
text("١٧", (245, 360), align="right")
text("١٨", (270, 379), align="right")
text("١٩", (298, 387), align="right")


tracking(None)

rotate(-15, center=(CENTER, CENTER))
text("بهاء", (298, 533), align="right")

rotate(-15, center=(CENTER, CENTER))
text("جلال", (325, 533), align="right")

rotate(-17, center=(CENTER, CENTER))
text("جمال", (327, 532), align="right")


rotate(-19, center=(CENTER, CENTER))
text("عظمة", (331, 530), align="right")

rotate(-16, center=(CENTER, CENTER))
text("نور", (335, 535), align="right")

rotate(82, center=(CENTER, CENTER))
rotate(82, center=(CENTER, CENTER))
text("رحمة", (300, 70), align="right")

rotate(-30, center=(CENTER, CENTER))
text("كلمات", (350, 65), align="right")

rotate(-19, center=(CENTER, CENTER))
text("كمال", (344, 65), align="right")

rotate(-19, center=(CENTER, CENTER))
text("اسماء", (344, 65), align="right")

rotate(-19, center=(CENTER, CENTER))
text("عزة", (344, 65), align="right")

rotate(-18, center=(CENTER, CENTER))
text("مشية", (344, 65), align="right")

rotate(-21, center=(CENTER, CENTER))
text("علم", (344, 65), align="right")

rotate(-17, center=(CENTER, CENTER))
text("قدرة", (344, 65), align="right")

rotate(-19, center=(CENTER, CENTER))
text("قول", (344, 65), align="right")

rotate(160, center=(CENTER, CENTER))
rotate(283, center=(CENTER, CENTER))
text("علاء", (298, 533), align="right")

rotate(19, center=(CENTER, CENTER))
text("ملك", (298, 533), align="right")

rotate(19, center=(CENTER, CENTER))
text("سلطان", (310, 529), align="right")

rotate(21, center=(CENTER, CENTER))
text("شرف", (310, 533), align="right")

rotate(19, center=(CENTER, CENTER))
text("مسائل", (310, 533), align="right")

saveImage("pdfs/176-mulk.pdf")
saveImage("images/176-mulk.png")
