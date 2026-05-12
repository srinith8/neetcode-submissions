class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(start: int, current: list[int]) -> None:
            # Every state of current is a valid subset
            result.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])          # choose
                backtrack(i + 1, current)         # explore
                current.pop()                     # un-choose (backtrack)

        backtrack(0, [])
        return result