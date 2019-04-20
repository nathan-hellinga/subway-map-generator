r = 25
grid = 10
count = 5

def setup():
    background(255)
    global p1
    global p2
    size(720, 720)
    
    
def draw_subway_line(p1, p2):
    strokeWeight(10)
    fill(255)
    stroke(220, 20, 20)
    mid_point = None
    if abs(p1[0] - p2[0]) < abs(p1[1] - p2[1]):
        if p2[1] < p1[1]:
            # down
            m = -1
        else:
            # up
            m = 1
        mid_point = (p2[0], m * abs(p1[0]-p2[0]) + p1[1])
    else:
        if p2[0] < p1[0]:
            # left
            m = -1
        else:
            # right
            m = 1
        mid_point = (m * abs(p2[1] - p1[1]) + p1[0], p2[1])
        
    # draw lines
    line(p1[0], p1[1], mid_point[0], mid_point[1])
    line(mid_point[0], mid_point[1], p2[0], p2[1])
    
    
def draw_station(p1, p2):
    ellipse(p1[0], p1[1], r, r)
    ellipse(p2[0], p2[1], r, r)
    
    
    
def generate_map():
    stations = []
    for i in range(count):
        p1 = int(random(grid - 1) + 1) * int(width / grid), int(random(grid - 1) + 1) * int(height / grid)
        p2 = int(random(grid - 1) + 1) * int(width / grid), int(random(grid - 1) + 1) * int(height / grid)
        # check to see if thye are the same point
        if p1[0] == p2[0] and p1[1] == p2[1]:
            continue
        draw_subway_line(p1, p2)
        stations.append((p1, p2))
    
    # draw stations on top
    for s in stations:
        draw_station(s[0], s[1])


def draw():
    frameRate(0.5)
    background(255)
    generate_map()

    
    
    
    
