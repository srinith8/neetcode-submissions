from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        # In LeetCode: [a, b] means you must take b before a (b -> a)
        for dest, src in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)
            
        q = deque(i for i, d in enumerate(indegree) if d == 0)
        order = []  # 1. Track the course sequence
        
        while q:
            curr = q.popleft()
            order.append(curr)  # 2. Record the course as you take it
            
            for ngbhr in adj[curr]:
                indegree[ngbhr] -= 1
                if indegree[ngbhr] == 0:
                    q.append(ngbhr)
                    
        # 3. If all courses are taken, return order; otherwise return []
        return order if len(order) == numCourses else []