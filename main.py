from map import GridMap
from astar import AStar
from view import MapView

def main():
    grid = GridMap(5, 5)

    blocks = [(0,0), (1,1), (2,2), (3,3)]
    for x, y in blocks:
        grid.set_block(x, y)

    start = grid.grid[1][3]
    end = grid.grid[3][0]

    astar = AStar(grid)
    path = astar.find_path(start, end)

    view = MapView(grid)
    view.render(path, start, end)

if __name__ == "__main__":
    main()