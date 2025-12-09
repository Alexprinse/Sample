import heapq
from typing import List
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        pq = []
        start = 0
        for t, end in courses:
            start += t
            heapq.heappush(pq,-t)
            while start > end:
                start += heapq.heappop(pq)
        return len(pq)
        
        