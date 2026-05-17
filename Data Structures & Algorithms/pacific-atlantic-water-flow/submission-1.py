class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, reachable):
            reachable[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Move to neighbor if it has equal or greater height (reverse flow)
                if 0 <= nr < m and 0 <= nc < n and not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reachable)

        # DFS from Pacific border (top row + left column)
        for c in range(n):
            dfs(0, c, pacific)
        for r in range(m):
            dfs(r, 0, pacific)

        # DFS from Atlantic border (bottom row + right column)
        for c in range(n):
            dfs(m - 1, c, atlantic)
        for r in range(m):
            dfs(r, n - 1, atlantic)

        # Collect cells reachable from both oceans
        result = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        return result