def setup():
    size (1200,720)
    global p1
    global p2
    global p3
    global p4
    global L1
    global L2
    global L3
    global L4
    p1 = 30
    p2 = 20
    p3 = 55
    p4 = 55
    L1 = 130
    L2 = 120
    L3 = p3
    L4 = p4
    
def keyPressed():
    if key == CODED:
        if keyCode == RIGHT:
            global p1
            global p2
            p1 = p1 + 10
            p2 = p2 
        if keyCode == LEFT:
            global p1
            global p2
            p1 = p1 - 10
            p2 = p2
        if keyCode == UP:
            global p1
            global p2
            p1 = p1
            p2 = p2 - 10
        if keyCode == DOWN:
            global p1
            global p2
            p1 = p1
            p2 = p2 + 10
            
#Deuxième joueur
           
    if key == 'd' :
        global L1
        global L2
        L1 = L1 + 10
        L2 = L2 
    if key == 'q':
        global L1
        global L2
        L1 = L1 - 10
        L2 = L2
    if key == 'z':
        global L1
        global L2
        L1 = L1
        L2 = L2 - 10
    if key == 's':
        global L1
        global L2
        L1 = L1
        L2 = L2 + 10




def draw():    
    background(0)
    rect(p1,p2,p3,p4)
    rect(L1,L2,L3,L4)