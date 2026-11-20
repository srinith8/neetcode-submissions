class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index=len(nums)-1
        maxreach=0
        for i,jump in enumerate(nums):
            if i>maxreach:
                return False 
            maxreach=max(maxreach,i+jump)
        return True


        