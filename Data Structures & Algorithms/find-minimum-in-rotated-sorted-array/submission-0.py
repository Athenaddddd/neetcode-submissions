class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            mid = (right - left)//2 + left

            if nums[mid] < result:
                result = nums[mid]

            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1

        return result
    