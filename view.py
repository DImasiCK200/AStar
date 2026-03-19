class MapView:
    def __init__(self, grid_map):
        self.map = grid_map

    def render(self, path, start, end):
        for y in range(self.map.height):
            row = ""
            for x in range(self.map.width):
                if (x, y) == (start.x, start.y):
                    row += "S "
                elif (x, y) == (end.x, end.y):
                    row += "E "
                elif not self.map.grid[x][y].walkable:
                    row += "B "
                elif (x, y) in path:
                    row += "o "
                else:
                    row += ". "
            print(row)