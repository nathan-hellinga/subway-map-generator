from route import Route

r = 25
grid = 10
count = 5
bg = color(250, 241, 220)

count = 1

def setup():
    background(bg)
    strokeWeight(10)
    global p1
    global p2
    size(720, 720)
    
    
def draw_subway_line(p1, p2):
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
    
    
def draw_station(p1):
    fill(bg)
    ellipse(p1[0], p1[1], r, r)
    
    
def save_image():
    global count
    save("assets/output_{:02d}.png".format(count))
    count += 1
        


def draw():
    frameRate(0.5)
    background(bg)
    routes = []
    for i in range(3):
        routes.append(Route(int(random(4)) + 2, grid))
        
    # draw lines
    for r in routes:
        stroke(r.col)
        for i in range(len(r.stations) -1):
            draw_subway_line(r.stations[i], r.stations[i + 1])
            
    for r in routes:
        stroke(r.col)
        for i in r.stations:
            draw_station(i)
            
    # save_image()

    
    
    
    
