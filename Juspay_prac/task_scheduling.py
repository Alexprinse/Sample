# from collections import deque
# class Solution():
#     def conv_to_graph(self,tasks,req):
#         n = len(req)
#         graph = {}
#         indegree = {}
#         for i in tasks:
#             graph[i] = []
#             indegree[i] = 0
        
#         for a,b in req:
#             graph[a].append(b)
#             indegree[b] += 1
        
#         return graph,indegree


#     def task_scheduling(self,task,req):
#         graph , indegree = self.conv_to_graph(task,req)

#         res = []
#         q = deque()

#         for node in indegree:
#             if indegree[node] == 0:
#                 q.append(node)

#         while q:
#             node = q.popleft()
#             res.append(node)
#             for neg in graph[node]:
#                 indegree[neg] -= 1
#                 if indegree[neg] == 0:
#                     q.append(neg)
#         return res if len(graph) == len(res) else None
    
# tasks = ["a", "b", "c", "d"]
# requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
# s = Solution()
# print(s.task_scheduling(tasks,requirements))

class Solution:
    def conv_to_graph(self,tasks,req):
        n = len(req)
        graph = {}
        for i in tasks:
            graph[i] = []
        
        for a,b in req:
            graph[a].append(b)
        
        return graph
    def task_scheduling(self,task,req):
        graph = self.conv_to_graph(task,req)
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

tasks = ["a", "b", "c", "d"]
requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
s = Solution()
print(s.task_scheduling(tasks,requirements))
    
    