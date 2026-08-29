class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        for i in range(0,len(s)):
            if s[i] in dic1:
                dic1[s[i]] = dic1[s[i]] + 1
            else:
                dic1[s[i]] = 1

        for j in range(0,len(t)):
            if t[j] in dic2:
                dic2[t[j]] = dic2[t[j]] + 1
            else:
                dic2[t[j]] = 1

        if dic1 == dic2:
            return True
        else:
            return False
