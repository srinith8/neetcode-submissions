from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helper(arr):
            @cache
            def dp(i):
                if i>=len(arr):
                    return 0
                return max(arr[i]+dp(i+2),dp(i+1))
            return dp(0)
        return max(
            helper(nums[:-1]),helper(nums[1:])
        )     