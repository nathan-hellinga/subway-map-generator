class Route:
        
    def generate_route(self, stops, grid):
        for i in range(stops):
            point = int(random(grid - 1) + 1) * int(width / grid), int(random(grid - 1) + 1) * int(height / grid)
            # don't add duplicate points
            if not self.check_point(point, self.stations):
                i -= 1
                continue
            self.stations.append(point)
            
            
    def check_point(self, p, check):
        for p2 in check:
            if p[0] == p2[0] and p[1] == p2[1]:
                return False
        return True
            
            
    def __init__(self, stops, grid):
        self.stations = []
        self.col = color(random(200) + 20, random(200) + 20, random(200) + 20)
        
        self.generate_route(stops, grid)
            
