class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])

        layers = min(m,n) // 2

        for layer in range(layers):
            top = layer
            bottom = m - 1 - layer
            left = layer
            right = n - 1 - layer

            values = []

            #top row
            for c in range(left, right + 1):
                values.append(grid[top][c])
            
            #right col
            for r in range(top + 1, bottom):
                values.append(grid[r][right])
            
            #bottom row
            for c in range(right, left - 1, - 1):
                values.append(grid[bottom][c])
            
            #left row
            for r in range(bottom - 1, top, -1):
                values.append(grid[r][left])
            
            l = len(values)
            rotate = k % l

            rotated = values[rotate:] + values[:rotate]

            index = 0

            # put back top row
            for c in range(left, right + 1):
                grid[top][c] = rotated[index]
                index += 1

            # put back right column
            for r in range(top + 1, bottom):
                grid[r][right] = rotated[index]
                index += 1

            # put back bottom row
            for c in range(right, left - 1, -1):
                grid[bottom][c] = rotated[index]
                index += 1

            # put back left column
            for r in range(bottom - 1, top, -1):
                grid[r][left] = rotated[index]
                index += 1

        return grid