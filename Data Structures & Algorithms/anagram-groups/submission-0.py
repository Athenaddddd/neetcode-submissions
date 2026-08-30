class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        
        for i in range(0,len(strs)):
            key = tuple(sorted(strs[i]))

            if key in seen:
                seen[key].append(strs[i])
            else:
                seen[key] = [strs[i]]

        return list(seen.values())


