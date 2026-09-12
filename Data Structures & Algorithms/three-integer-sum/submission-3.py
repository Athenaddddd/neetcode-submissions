class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            need = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
        
                if nums[left] + nums[right] == need:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] < need:
                    left += 1
                elif nums[left] + nums[right] > need:
                    right -= 1
                
        return result







        