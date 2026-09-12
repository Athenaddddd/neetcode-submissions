class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove duplicates, also fast to find in sets
        orig = set()
        for i in range(len(nums)):
            orig.add(nums[i])

        starts = []
        for j in orig:
            if j - 1 in orig:
                continue
            else:
                starts.append(j)
            

        maxlen = 0
        for k in range(len(starts)):
            currnum = starts[k]
            currlen = 1
            
            while currnum + 1 in orig:
                currlen = currlen + 1
                currnum += 1
            maxlen = max(currlen, maxlen)
        
        return maxlen

