class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = ""
 
        for i in range(0, len(strs)):
            length = len(strs[i])
            encoded += str(length) + "@" + strs[i]
        return encoded


    def decode(self, s: str) -> List[str]:

        result = []

        start = 0
        while start < len(s):
            p = start
            r = start

            while s[r] != "@":
                r = r+1
            count = int(s[p:r])
            start = r + 1

            curr = ""
            while count > 0:
                curr += s[start]
                start = start + 1
                count = count - 1
            result.append(curr)

        return result
        

