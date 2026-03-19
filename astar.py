class AStar:
    def __init__(self, grid_map):
        self.map = grid_map

    def heuristic(self, a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

    def find_path(self, start, end):
        open_list = [start] 
        closed_set = set()

        start.g = 0
        start.h = self.heuristic(start, end)
        start.f = start.h

        while open_list:
            current = min(open_list, key=lambda n: n.f)

            if current == end:
                return self._reconstruct_path(end)

            open_list.remove(current)
            closed_set.add((current.x, current.y))

            for neighbor in self.map.get_neighbors(current):
                if (neighbor.x, neighbor.y) in closed_set:
                    continue

                tentative_g = current.g + 1

                if neighbor not in open_list:
                    open_list.append(neighbor)

                elif tentative_g >= neighbor.g:
                    continue

                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.h = self.heuristic(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h

        return []

    def _reconstruct_path(self, end):
        path = []
        current = end
        while current:
            path.append((current.x, current.y))
            current = current.parent
        return path[::-1]