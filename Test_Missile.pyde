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


Hauteur = 800
Largeur = 600

def keyPressed():           
    if key == '6' :
        global Player_x
        global Player_y
        Player_x = Player_x + 10
        Playery = Player_y 
    if key == '4':
        global Player_x
        global Player_y
        Player_x = Player_x - 10
        Player_y = Player_y
    if key == '8':
        global Player_x
        global Player_y
        Player_x = Player_x
        Player_y = Player_y - 10
        if Player_y<1:
            Player_y = 1
    if key == '2':
        global Player_x
        global Player_y
        Player_x = Player_x
        Player_y = Player_y + 10
        if Player_y>Hauteur-58:
            Player_y=Hauteur-58
    if key == '7' :
        global Player_x
        global Player_y
        Player_x = Player_x - 10
        Player_y = Player_y - 10
        if Player_y<1:
            Player_y=1
    if key == '9' :
        global Player_x
        global Player_y
        Player_x = Player_x + 10
        Player_y = Player_y - 10
        if Player_y<1:
            Player_y=1
    if key == '1' :
        global Player_x
        global Player_y
        Player_x = Player_x - 10
        Player_y = Player_y + 10
        if Player_y>Hauteur-58:
            Player_y=Hauteur-58
    if key == '3' :
        global Player_x
        global Player_y
        Player_x = Player_x + 10
        Player_y = Player_y + 10
        if Player_y>Hauteur-58: 
            Player_y=Hauteur-58
#    if key == ' ' :
#        if not tirEnCours :
 #           tirEnCours = True
        
#def gere_missile():
    """
    je retrouve la position du missile qui est une variable globale
    je l'actualise
    je décide si le tir est fini, auquel cas je remetes tirEnCours à False
    """
    
    rect(Missile_x,Missile_y,Missile_l,Missile_h)

def draw():
    background(0)
#    if tirEnCours:
#        gere_missile()
        
#        print('oke')

#    rect(px,py,pl,ph)
    rect(Player_x,Player_y,Player_l,Player_h)
    if Player_x > Largeur:
        global Player_x
        Player_x = Largeur-650
    if Player_x < Largeur-660:
        global Player_x
        Player_x = Largeur-10