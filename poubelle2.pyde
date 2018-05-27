def setup():
    global Largeur
    global Hauteur
    size (Largeur,Hauteur)
    
    global Testx
    global Testy
    global Testl
    global Testh
    
    global Player_x
    global Player_y
    global Player_l
    global Player_h
   
    global Colision_x
    global Colision_y
    
    Colision_x = False
    Colision_y = False
    
    Testx = 30
    Testy = 20
    Testl = 55
    Testh = 55
    
    Player_x = 130
    Player_y = 742
    Player_l = Testl
    Player_h = Testh
  
    global posX
    global posY
    global depX
    global depY
    posX = 10 + random(Largeur - 10)
    posY = 0
    depX = -5 + random(5)
    depY = -5 + random(5)
    while depX == 0 or depY == 0:
        depX = -5 + random(5)
        depY = -5 + random(5)
    

def depEnemie(a, b, c, d):
    global posX, posY, depX, depY
    if posX < 0 or posX > Largeur - 55:
        depX = -depX
    posY += depY
    if posY < 0 :
        depY = -depY
    posX = posX + depX
    posY = posY + depY
    

posH = 55
posL = 55
    
Hauteur = 800
Largeur = 600



def keyPressed():           
    if key == '6' :
        global Player_x
        global Player_y
        Player_x = Player_x + 30
        Playery = Player_y 
    if key == '4':
        global Player_x
        global Player_y
        Player_x = Player_x - 30
        Player_y = Player_y
    if key == '8':
        global Player_x
        global Player_y
        Player_x = Player_x
        Player_y = Player_y - 30
        if Player_y<1:
            Player_y = 1
    if key == '5':
        global Player_x
        global Player_y
        Player_x = Player_x
        Player_y = Player_y + 30
        if Player_y>Hauteur-58:
            Player_y=Hauteur-58
    if key == '7' :
        global Player_x
        global Player_y
        Player_x = Player_x - 30
        Player_y = Player_y - 30
        if Player_y<1:
            Player_y=1
    if key == '9' :
        global Player_x
        global Player_y
        Player_x = Player_x + 30
        Player_y = Player_y - 30
        if Player_y<1:
            Player_y=1
    if key == '1' :
        global Player_x
        global Player_y
        Player_x = Player_x - 30
        Player_y = Player_y + 30
        if Player_y>Hauteur-58:
            Player_y=Hauteur-58
    if key == '3' :
        global Player_x
        global Player_y
        Player_x = Player_x + 30
        Player_y = Player_y + 30
        if Player_y>Hauteur-58: 
            Player_y=Hauteur-58

def draw():
    background(0)
    fill(255,0,0)
    
    global posX, posY
    rect(posX, posY, 55, 55)
    depEnemie(posX, posY, 55, 55)
    
    for i in range(0 , 800 + 55):
        global posX, posL
        if posX < Missile_x < posX + 55:
                global Colision_x
                Colision_x = True
                
    for i in range(0 , 800 + 55):
        global posY, posH, Missile_y
        if posY < Missile_y < posY + 55:
            global Colision_y
            Colision_y = True
    
    global Colision_x, Colision_y
    if Colision_x == True and Colision_y == True:
        print("HIT")
        Colision_x = False
        Colision_y = False
        clear()

#    rect(px,py,pl,ph)
    global Player_x
    rect(Player_x,Player_y,Player_l,Player_h)
    if Player_x > Largeur:
        Player_x = Largeur-650
    if Player_x < Largeur-660:
        Player_x = Largeur-10
