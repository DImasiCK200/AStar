class Node:
    def __init__(self, x, y, walkable=True):
        self.x = x
        self.y = y
        self.walkable = walkable
        
        self.g = float('inf')  # стоимость от старта
        self.h = 0             # эвристика до цели
        self.f = float('inf')  # g + h
        
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f