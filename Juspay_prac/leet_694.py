class Solution:
    def distinct_island(self,grid:list):
        m, n = len(grid), len(grid[0])

        path = []

        unique_p = set()

        def dfs(i,j,k):
            grid[i][j] = 0
            path.append(str(k))

            dirc = (-1, 0, 1, 0, -1)
            for h in range(1,5):
                nr, nc = i + dirc[h-1], j + dirc[h]
                if (0 <= nr < m and
                    0 <= nc < n and
                    grid[nr][nc] == 1):
                    dfs(nr,nc,h)
            path.append(str(-k))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j,0)
                    unique_p.add("".join(path))
                    path.clear()
        print(unique_p)
        return(len(unique_p))
    
grid = [[1,0,1],[1,0,1],[0,1,1]]
s = Solution()
print(s.distinct_island(grid))
                 