from collections import deque 
class Solution:
    def Bipartite(self,graph:list) -> bool:
        n = len(graph)
        color = [-1] * n
        q = deque()

        for i in range(n):
            if color[i] != -1:
                continue
            q.append(i)
            color[i] = 0

            while q:
                u = q.popleft()
                cc = color[u]
                for j in graph[u]:
                    if color[j] == -1:
                        color[j] = 1 - cc
                        q.append(j)
                    if color[j] == cc:
                        return False

        
        return True

S = Solution()
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
g2 = [[1,3],[0,2],[1,3],[0,2]]
print(S.Bipartite(graph))
print(S.Bipartite(g2))
