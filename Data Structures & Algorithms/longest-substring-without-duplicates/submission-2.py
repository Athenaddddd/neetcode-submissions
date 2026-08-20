class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        seen = set()
        left = 0

        for i in range(0,len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left = left + 1
            seen.add(s[i])
            maxlength = max(maxlength, len(seen))

        return maxlength
        





            
        