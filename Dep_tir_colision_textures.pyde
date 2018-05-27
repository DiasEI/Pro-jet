def setup():
    
    frameRate(60)
    global Largeur, Hauteur
    size (Largeur,Hauteur)
    
    global yImg1, yImg2, img, img1, img2
    
    yImg1 = 0
    yImg2 = -800
    img = loadImage("ship.png")
    img1 = loadImage("SpaceBackG1.jpeg")
    img2 = loadImage("SpaceBackG1.jpeg")
    
    global Testx, Testy, Testl, Testh
    
    global Player_x, Player_y, Player_l, Player_h
    
    global Missile_x, Missile_y, Missile_l, Missile_h
    
    global tirEnCours
   
    global Colision_x, Colision_y
    
    Colision_x = False
    Colision_y = False
    
    tirEnCours = False
    
    Testx = 30
    Testy = 20
    Testl = 55
    Testh = 55
    
    Player_x = 130
    Player_y = 742
    Player_l = Testl
    Player_h = Testh
    
    Missile_x = Player_x +22.5
    Missile_y = Player_y -50
    Missile_l = 10
    Missile_h = 55
  
    global posX, posY, depX, depY
    posX = 10 + random(Largeur - 55)
    posY = 1 - 100
    depX = -5 + random(5)
    depY = -5 + random(5)
    #posX = 500
    #posY = 300
    while depX == 0 or depY == 0:
        depX = -5 + random(5)
        depY = -5 + random(5)
    

def depEnemie(a, b, c, d):
    global posX, posY, depX, depY
    if posX < 0 or posX > Largeur - 55:
        depX = -depX
    if posY < 1 - 100:
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
    if key == 'g' :
        global tirEnCours
        if not tirEnCours :
            tirEnCours = True
            global Missile_x
            global Missile_y
            Missile_x = Player_x +22.5
            Missile_y = Player_y -50
            
def gere_missile():
    """
    je retrouve la position du missile qui est une variable globale
    je l'actualise
    je décide si le tir est fini, auquel cas je remetes tirEnCours à False
    """
    global Missile_x, Missile_y, Missile_h, Missile_h

    global Player_x, Player_y, posX, posY, posL, posH

    global tirEnCours

    if Missile_y < 1 - Missile_h :
        tirEnCours = False
    if 250 < Missile_x < 250 +55 and 100 < Missile_y < 100 -55 :
        tirEnCours = False
    else :
        Missile_y = Missile_y - 25
        
    rect(Missile_x,Missile_y,Missile_l,Missile_h)

def draw():
    
    global yImg1, yImg2, Lx, Ly
    
    y1 = yImg1 % 800
    y2 = yImg2 % -800
    image(img1, 0, y1)
    image(img2, 0, y2)
    yImg1 = yImg1 + 0.742
    yImg2 = yImg2 + 0.742
    
    global posX, posY, posL, posH
    
    global Player_x, Player_y
    
    rect(posX, posY, 55, 55)
    depEnemie(posX, posY, 55, 55)
    
    global tirEnCours
    if tirEnCours:
        gere_missile()
        
    global Missile_x, Colision_x, Colision_y

    if posX - 5 < Missile_x < posX + 55:
        Colision_x = True
    else:
        Colision_x = False
                
    if posY < Missile_y < posY + 55:
        Colision_y = True
    else:
        Colision_y = False
        
    global Colision_Xdroit, Colision_Xgauche, Collision_Ybas, Collision_Yhaut    
        
    if Player_x < posX < Player_x + 55:
        Colision_Xdroit = True
                
    else:
        Colision_Xdroit = False
        
    if Player_x -55 < posX < Player_x :
        Colision_Xgauche = True
                
    else:
        Colision_Xgauche = False
            
    if Player_y < posY < Player_y + 55:        
        Colision_Ybas = True
            
    else:
        Colision_Ybas = False
        
    if Player_y -55 < posY < Player_y :        
        Colision_Yhaut = True
            
    else:
        Colision_Yhaut = False
        
    
    if Colision_Xdroit == True and Colision_Ybas == True:
        print("HIT BD")
        clear()
    
    elif Colision_Xdroit == True and Colision_Yhaut == True:
        print("HIT HD")
        clear()
        
    elif Colision_Xgauche == True and Colision_Ybas == True:
        print("HIT BG")
        clear()

    elif Colision_Xgauche == True and Colision_Yhaut == True:
        print("HIT HG")
        clear()
        
    else:
        Colision_Xgauche = False
        Colision_Yhaut = False
        Colision_Xdroit = False
        Colision_Ybas = False    

    if Colision_x == True and Colision_y == True:
        Colision_x = False
        Colision_y = False
        posX = 10 + random(Largeur - 55)
        posY = 1 - 100
        depX = -5 + random(5)
        depY = -5 + random(5)
        
    if posY > 800:
       posY = 1 - 100
    
    global Player_x
    
    image(img, Player_x, Player_y, Player_l, Player_h)
    
    if Player_x > Largeur:
        Player_x = Largeur-650
    if Player_x < Largeur-660:
        Player_x = Largeur-10
        
