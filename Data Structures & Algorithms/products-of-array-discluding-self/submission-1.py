class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        before = 1
        after = 1

        for i in range(0,len(nums)):
            result.append(before)
            before = before * nums[i]

        for j in range(len(nums) -1 , -1, -1):
            result[j] = result[j] * after
            after = after * nums[j]

        return result
