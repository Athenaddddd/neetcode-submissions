class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        for i in range(0,len(s)):
            dic1[s[i]] = dic1.get(s[i],0) + 1

        for j in range(0,len(t)):
            dic2[t[j]] = dic2.get(t[j],0) + 1

        if dic1 == dic2:
            return True
        else:
            return False
