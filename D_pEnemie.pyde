Largeur = 600
Hauteur = 800


def setup():
    size(Largeur, Hauteur)
    global posX
    global posY
    global depX
    global depY
    posX = 10 + random(Largeur - 10)
    posY = 10 + random(190)
    depX = -5 + random(5)
    depY = -5 + random(5)
    while depX == 0 or depY == 0:
        depX = -5 + random(5)
        depY = -5 + random(5)
    
    
def depEnemie(a, b, c, d):
    global posX
    global posY
    global depX
    global depY
    if posX < 0 or posX > Largeur - 55:
        depX = -depX
    if posY < 0 or posY > 190:
        depY = -depY
    posX = posX + depX
    posY = posY + depY


def draw():
    background(0)
    global posX
    global posY
    rect(posX, posY, 55, 55)
    depEnemie(posX, posY, 55, 55)