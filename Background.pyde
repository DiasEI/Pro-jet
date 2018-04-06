yImg1 = 0
yImg2 = -800

def setup():
    size (600,800)
    global img1
    global img2
    img1 = loadImage("SpaceBackG1.jpeg")
    img2 = loadImage("SpaceBackG1.jpeg")
    frameRate(60)
    
def draw():
    background(0)
    global yImg1
    global yImg2
    y1 = yImg1 % 800
    y2 = yImg2 % -800
    image(img1, 0, y1)
    image(img2, 0, y2)
    yImg1 = yImg1 + 0.5
    yImg2 = yImg2 + 0.5
    