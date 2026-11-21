from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(rem):
            if rem == 0: return 0              # 1. Exact hit
            if rem < 0:  return float('inf')   # 2. Overshot (bad path)
            
            # 3. Try every coin + 1, take the minimum
            return min(1 + dp(rem - c) for c in coins)
            
        ans = dp(amount)
        return ans if ans != float('inf') else -1
        