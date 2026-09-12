class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            h = min(heights[left],heights[right])
            water = h * (right - left)
            maxwater = max(maxwater, water)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxwater

        