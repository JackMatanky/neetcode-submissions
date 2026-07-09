class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output: list[int] = [1] * len(nums)
        
        prefix: int = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        postfix: int = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output