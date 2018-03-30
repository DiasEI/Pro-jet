y = 0

def setup():
    size (600,800)
    global img
    img = loadImage("SpaceBackG.jpeg")
    frameRate(60)
    
def draw():
    background(0)
    global y
    y = y + 1%800
    image(img, 0, y)