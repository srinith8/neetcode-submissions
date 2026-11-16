from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[0] = dist[k] = 0  # Setting dist[0] = 0 avoids slicing dist[1:] later

        for i in range(n):
            updated = False
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    if i == n - 1:
                        return -1
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break

        res = max(dist)
        return res if res < INF else -1