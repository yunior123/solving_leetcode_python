

def numIslands(grid) -> int:
    islandCount = 0
    visited = set()

    r=0
    c=0
    for _ in grid:
        r+=1
        for _ in grid[0] :
            c+=1
            if explore(grid, r, c, visited):
                islandCount += 1
    return islandCount


def explore(
 grid,
 x,
 y,
 visited: set
) :
    rowBounds = 0 <= x and x < len(grid)
    columnBounds = 0 <= y and y < len(grid[0])
    if not rowBounds and not columnBounds:
        return False
    position = "{0},{1}".format(x,y)
    if position in visited:
        return False

    visited.add(position)

    explore(grid, x - 1, y, visited)
    explore(grid, x + 1, y,visited)
    explore(grid, x, y - 1,visited)
    explore(grid, x, y + 1,visited)
    return True

print(numIslands(
     [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))