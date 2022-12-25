def island_count(grid):
    visited = set()
    count = 0
    
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if  explore(grid, row, column, visited) == True: 
                count += 1
    return count


def explore(grid, row, column, visited):
    row_inbounds = 0 <= row and row < len(grid)
    column_inbounds = 0 <= column and column < len(grid[0])
    if not row_inbounds or not column_inbounds: return False

    if grid[row][column] == 'W': return False

    current_position = str(row) +',' + str(column)

    if current_position in visited: return False

    visited.add(current_position)

    explore(grid, row -1, column, visited) # go up
    explore(grid, row + 1, column, visited) # go down
    explore(grid, row , column -1, visited) # go lefts
    explore(grid, row , column +1, visited) # go right

    return True





grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
   [ "W", "W", "W", "L", "W"],
    [ "W", "W", "L", "L", "W"],
     [ "L", "W", "W", "L", "L"],
      [ "L", "L", "W", "W", "W"]
]

print(island_count(grid))