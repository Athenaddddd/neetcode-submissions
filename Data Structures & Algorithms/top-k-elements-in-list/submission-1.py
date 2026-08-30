class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}
        result = []

        for i in range(0, len(nums)):
            seen[nums[i]] = seen.get(nums[i] , 0) + 1

        sortedkeys = sorted(seen, key=seen.get, reverse = True)
        result = sortedkeys[:k]

        return result
        