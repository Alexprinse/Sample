from collections import deque,defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = defaultdict(list)
        indeg = [0] * numCourses
        for i, j in prerequisites:
            adj[j].append(i)
            indeg[i] += 1

        q = deque()
        res = []

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            res.append(u)
            for i in adj[u]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        
        return res if len(res) == numCourses else []




        