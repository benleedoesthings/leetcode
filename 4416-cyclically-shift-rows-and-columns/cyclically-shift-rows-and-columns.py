class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        """
        1 2
        3 4
        """

        res = [[0 for i in range(n)] for i in range(n)]

        for i in range(n):
            shift = rowShift[i]
            for j in range(n):
                res[i][j] = grid[i][(j + shift) % n]

        #print(res)
    
        grid = res
        res = [[0 for i in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                shift = colShift[j]
                res[i][j] = grid[(i + shift) % n][j]
                #print(res)

        return res