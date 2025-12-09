from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for node in range(numCourses)]
        indegree = [0] * numCourses
        for i , j in prerequisites:
            adj[j].append(i)
            indegree[i] += 1

        out = 0
        q = deque()

        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            u = q.popleft()
            for i in adj[u]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
            out += 1

        return numCourses == out



        