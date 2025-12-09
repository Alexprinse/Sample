class Solution:
    def topological_sort_dfs(self,graph):
        def dfs(node,visit,res,stack):
            visit.add(node)
            res.add(node)

            for neg in graph[node]:
                if neg not in visit:
                    dfs(neg,visit,res,stack)


            res.remove(node)
            stack.append(node) 
            return True

        visit = set()
        res = set()
        stack = []

        for i in graph:
            if i not in visit:
                if not dfs(i,visit,res,stack):
                    return None
        
        return stack[::-1]
    
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': [],
    'E': ['B']
}

s = Solution()
print(s.topological_sort_dfs(graph))
    
graph_with_cycle = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [2]
}
result = s.topological_sort_dfs(graph_with_cycle)
print(result) 