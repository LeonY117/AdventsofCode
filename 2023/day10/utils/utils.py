def invert(coord):
    return (-coord[0], -coord[1])


def add(coord1, coord2):
    """adds two tuples element wise"""
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])


def isWithinBounds(coord, grid):
    """checks if a coordinate is within the grid"""
    return 0 <= coord[0] < len(grid[0]) and 0 <= coord[1] < len(grid)


def isOnBound(coord, grid):
    """checks if a coordinate is on the boundary of the grid"""
    return (
        coord[0] == 0
        or coord[0] == len(grid[0]) - 1
        or coord[1] == 0
        or coord[1] == len(grid) - 1
    )


def print_grid(grid):
    [print("".join(row)) for row in grid]
    return 
