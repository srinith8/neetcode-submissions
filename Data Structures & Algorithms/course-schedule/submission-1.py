from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
            
        q = deque(i for i, d in enumerate(indegree) if d == 0)
        
        while q:
            for nei in adj[q.popleft()]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)
                    
        return not any(indegree)