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
                curr = []
                if nums[left] + nums[right] == need:
                    curr.append(nums[i])
                    curr.append(nums[left])
                    curr.append(nums[right])
                    if curr not in result:
                        result.append(curr)
                    left += 1
                elif nums[left] + nums[right] < need:
                    left += 1
                elif nums[left] + nums[right] > need:
                    right -= 1
                
        return result







        