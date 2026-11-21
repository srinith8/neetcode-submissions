from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dp(rem):
            if rem == 0:
                return 0

            if rem < 0:
                return float('inf')

            ans = float('inf')

            for coin in coins:
                ans = min(ans, 1 + dp(rem - coin))

            return ans

        res = dp(amount)
        return res if res != float('inf') else -1