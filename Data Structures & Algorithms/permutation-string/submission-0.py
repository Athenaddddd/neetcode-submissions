class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        orig = {}
        left = 0

        for j in range(0,len(s1)):
            if s1[j] in orig:
                orig[s1[j]] = orig[s1[j]] + 1
            else:
                orig[s1[j]] = 1

        for i in range(0,len(s2)):

            if s2[i] in count:
                count[s2[i]] = count[s2[i]] + 1
            else:
                count[s2[i]] = 1

            while sum(count.values()) > len(s1):
                count[s2[left]] = count[s2[left]] - 1
                if count[s2[left]] == 0:
                    del count[s2[left]]
                left = left + 1

            if count == orig:
                return True
        
        return False



        