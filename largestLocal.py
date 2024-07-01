class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
    
        for i in range(n - 2):
            for j in range(n - 2):
                local_max = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        local_max = max(local_max, grid[x][y])
                maxLocal[i][j] = local_max
    
        return maxLocal
