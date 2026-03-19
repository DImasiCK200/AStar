from map import GridMap
from astar import AStar
from view import MapView

def main():
    grid = GridMap(10, 5)

    blocks = [(8, 0), (8, 1), (8, 2), (8, 3),
              (6, 4), (6, 3), (6,2 ),
              (2, 0), (2, 1), (2, 2),
              (1, 2)]
    for x, y in blocks:
        grid.set_block(x, y)

    start = grid.grid[1][1]
    end = grid.grid[9][0]

    astar = AStar(grid)
    path = astar.find_path(start, end)

    view = MapView(grid)
    view.render(path, start, end)

if __name__ == "__main__":
    main()