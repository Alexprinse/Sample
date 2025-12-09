class Solution:
    def Bipartite(self,graph:list) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(n, c):
            color[n] = c
            for i in graph[n]:
                if color[i] == -1:
                    if not dfs(i, 1-c ):
                        return False

                elif color[i] == c:
                    return False
                
            return True
        
        for i in range(n):
            if color[i] == -1:
                if not dfs(i,0):
                    return False
        
        return True

S = Solution()
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
g2 = [[1,3],[0,2],[1,3],[0,2]]
print(S.Bipartite(graph))
print(S.Bipartite(g2))
