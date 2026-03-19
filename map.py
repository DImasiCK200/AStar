from node import Node

class GridMap:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.grid = [[Node(x, y) for y in range(height)] for x in range(width)]

    def set_block(self, x, y):
        self.grid[x][y].walkable = False

    def get_neighbors(self, node):
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        neighbors = []

        for dx, dy in directions:
            nx, ny = node.x + dx, node.y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbor = self.grid[nx][ny]
                if neighbor.walkable:
                    neighbors.append(neighbor)
        return neighbors