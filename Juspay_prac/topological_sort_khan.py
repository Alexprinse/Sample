from collections import deque
class Solution():
    def find_indegree(self,graph):
        indegree = {node : 0 for node in graph}
        for node in graph:
            for neg in graph[node]:
                indegree[neg] += 1
        return indegree
    def topo_sort_khan(self,graph):
        res = []
        q = deque()
        indegree = self.find_indegree(graph)
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)
        while q:
            node = q.popleft()
            res.append(node)
            for neg in graph[node]:
                indegree[neg] -= 1
                if indegree[neg] == 0:
                    q.append(neg)
        return res if len(graph) == len(res) else None

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['D'],
#     'D': [],
#     'E': ['B']
# }

# s = Solution()
# print(s.topo_sort_khan(graph))

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
sol = Solution()
result = sol.topo_sort_khan(graph)
print(result)  # Output: [0, 1, 2, 3] or [0, 2, 1, 3] (both valid)

# Graph with a cycle
graph_with_cycle = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [2]
}
result = sol.topo_sort_khan(graph_with_cycle)
print(result)  # Output: None (cycle detected)