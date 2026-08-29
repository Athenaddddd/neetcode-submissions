class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(0,len(nums)):
            
            need = target - nums[i]

            if need in seen:
                result = seen[need]
                break
            else:
                seen[nums[i]] = i

        return [result,i]
