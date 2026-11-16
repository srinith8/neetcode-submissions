class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        def find(node):
            while node!=parent[node]:
                parent[node]=parent[parent[node]]
                node=parent[node]
            return node
        for u,v in edges:
            root_u=find(u)
            root_v=find(v)
            if root_u==root_v:
                return [u,v]
            else:
                parent[root_u]=root_v
        return []

        