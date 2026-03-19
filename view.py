class MapView:
    def __init__(self, grid_map):
        self.map = grid_map

    def render(self, path, start, end):
        for y in range(self.map.height):
            row = ""
            for x in range(self.map.width):
                if (x, y) == (start.x, start.y):
                    row += "🟢"
                elif (x, y) == (end.x, end.y):
                    row += "🔴"
                elif not self.map.grid[x][y].walkable:
                    row += "◻️ "
                elif (x, y) in path:
                    row += "🟡"
                else:
                    row += "❍ "
            print(row)