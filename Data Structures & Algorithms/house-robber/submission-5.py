from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        @cache
        def dp(i):
            if i>=n:
                return 0
            return max(nums[i]+dp(i+2),dp(i+1))
        return dp(0)

        