class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        for i in range(len(s)):
            curr = s[i]
            seen = set()
            seen.add(curr)
            j = i + 1
            count = 1

            while j<len(s) and s[j] not in seen:
                count = count + 1
                seen.add(s[j])
                j = j+1

            if count > longest :
                longest = count

        return longest

            




        