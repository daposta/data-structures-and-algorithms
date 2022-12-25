def min_island_count(grid):
    visited = set()
    min_size = len(grid)
    print('min_size', min_size)
    
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            current_size = explore_size(grid, row, column, visited) 
            if current_size > 0 and   current_size < min_size: 
                min_size = current_size
    return min_size


def explore_size(grid, row, column, visited):
    row_inbounds = 0 <= row and row < len(grid)
    column_inbounds = 0 <= column and column < len(grid[0])
    if not row_inbounds or not column_inbounds: return 0

    if grid[row][column] == 'W': return 0

    current_position = str(row) +',' + str(column)

    if current_position in visited: return 0

    visited.add(current_position)

    size = 1

    size += explore_size(grid, row -1, column, visited) # go up
    size += explore_size(grid, row + 1, column, visited) # go down
    size += explore_size(grid, row , column -1, visited) # go lefts
    size +=explore_size(grid, row , column +1, visited) # go right

    print('size',size)

    return size





grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
   [ "W", "W", "W", "L", "W"],
    [ "W", "W", "L", "L", "W"],
     [ "L", "W", "W", "L", "L"],
      [ "L", "L", "W", "W", "W"]
]

print(min_island_count(grid))