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
    
    global Missile_x
    global Missile_y
    global Missile_l
    global Missile_h
    
    global tirEnCours
   
    global Colision_x
    global Colision_y
    
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
  
    global posX
    global posY
    global depX
    global depY
    posX = 10 + random(Largeur - 10)
    posY = 10 + random(190)
    depX = -5 + random(5)
    depY = -5 + random(5)
    #posX = 500
    #posY = 300
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
    if key == '2':
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
    global Missile_x
    global Missile_y
    global Missile_l
    global Missile_h
    global Player_x
    global Player_y
    global tirEnCours
    global posX
    global posY
    global posL
    global posH
#    Missile_x = Player_x +22.5
#    Missile_y = Player_y - 50
    if Missile_y < 200 - Missile_h :
        tirEnCours = False
#        print ("Bonjo")
    if 250 < Missile_x < 250 +55 and 100 < Missile_y < 100 -55 :
        tirEnCours = False
    else :
        Missile_y = Missile_y - 25
#    if tirEnCours = False:
        
    
        rect(Missile_x,Missile_y,Missile_l,Missile_h)

def draw():
    background(0)
    fill(255,0,0)
    rect(250,100,55,55)
    
    global posX
    global posY
    #rect(posX, posY, 55, 55)
    depEnemie(posX, posY, 55, 55)
    
    global tirEnCours
    if tirEnCours:
        gere_missile()
        
    global posX
    global posL
    global Missile_x
    
    for i in range(0 , 800 + 55):
        global posX
        global posL
        global Missile_x
        if 250 < Missile_x < 250 + 55:
                global Colision_x
                Colision_x = True
                
    global posY
    global posH
    global Missile_y 
    for i in range(0 , 800 + 55):
        global posY
        global posH
        global Missile_y
        if 100 < Missile_y < 100 + 55:
            global Colision_y
            Colision_y = True
    
    
    global Colision_x
    global Colision_y
    if Colision_x == True and Colision_y == True:
        print("HIT")
        Colision_x = False
        Colision_y = False
        clear()

#    rect(px,py,pl,ph)
    rect(Player_x,Player_y,Player_l,Player_h)
    
    if Player_x > Largeur:
        global Player_x
        Player_x = Largeur-650
    if Player_x < Largeur-660:
        global Player_x
        Player_x = Largeur-10
