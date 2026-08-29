class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        for i in range(0,len(nums)):
            if nums[i] in arr:
                return True
            else:
                arr.append(nums[i])

        return False
        