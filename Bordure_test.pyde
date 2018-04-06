def setup():
    global Largeur
    global Hauteur
    size (Largeur,Hauteur)
    global px
    global py
    global p3
    global p4
    global Lx
    global Ly
    global L3
    global L4
    px = 30
    py = 20
    p3 = 55
    p4 = 55
    Lx = 130
    Ly = 742
    L3 = p3
    L4 = p4

Hauteur = 800
Largeur = 600

def keyPressed():           
    if key == '6' :
        global Lx
        global Ly
        Lx = Lx + 10
        Ly = Ly 
    if key == '4':
        global Lx
        global Ly
        Lx = Lx - 10
        Ly = Ly
    if key == '8':
        global Lx
        global Ly
        Lx = Lx
        Ly = Ly - 10
        if Ly<1:
            Ly = 1
    if key == '2':
        global Lx
        global Ly
        Lx = Lx
        Ly = Ly + 10
        if Ly>Hauteur-58:
            Ly=Hauteur-58
    if key == '7' :
        global Lx
        global Ly
        Lx = Lx - 10
        Ly = Ly - 10
        if Ly<1:
            Ly=1
    if key == '9' :
        global Lx
        global Ly
        Lx = Lx + 10
        Ly = Ly - 10
        if Ly<1:
            Ly=1
    if key == '1' :
        global Lx
        global Ly
        Lx = Lx - 10
        Ly = Ly + 10
        if Ly>Hauteur-58:
            Ly=Hauteur-58
    if key == '3' :
        global Lx
        global Ly
        Lx = Lx + 10
        Ly = Ly + 10
        if Ly>Hauteur-58:
            Ly=Hauteur-58




def draw():    
    background(0)
#    rect(p1,p2,p3,p4)
    rect(Lx,Ly,L3,L4)
    if Lx > Largeur:
        global Lx
        Lx = Largeur-650
    if Lx < Largeur-660:
        global Lx
        Lx = Largeur-10
