from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build adjacency list and track in-degrees
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        # Initialize queue with courses having no prerequisites
        q = deque([i for i, d in enumerate(indegree) if d == 0])
        
        # Process the graph
        while q:
            for nei in adj[q.popleft()]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    
        # If any indegree is not 0, a cycle exists
        return sum(indegree) == 0