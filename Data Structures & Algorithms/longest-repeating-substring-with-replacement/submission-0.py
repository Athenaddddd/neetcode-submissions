class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlength = 0
        left = 0
        count = {}

        for i in range(0,len(s)):

            if s[i] in count:
                count[s[i]] = count[s[i]] + 1
            else:
                count[s[i]] = 1

            while (i - left + 1) - max(count.values()) > k :
                count[s[left]] = count[s[left]] - 1
                left = left + 1
            
            maxlength = max(maxlength, i-left+1)
        
        return maxlength






                

                


            




        