def setup():
    size(700, 450)
    background(100)
    colorMode(RGB, 20, 25, 700)
    noStroke()
    ellipseMode(RADIUS)
    frameRate(5)
    
def draw():
    background(0)
    for x in range(2, width + 1, width / 2):
        drawGradient(x, height / 2)


def drawGradient(x, y):
    radius = width / 1
    h = random(0, 360)
    for r in range(radius, 0, -1):
        fill(h, 90, 90)
        ellipse(x, y, r, r)
        h = (h + 1) % 40
