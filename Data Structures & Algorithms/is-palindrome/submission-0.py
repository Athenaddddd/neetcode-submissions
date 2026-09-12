class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = []
        for j in range (len(s)):
            if s[j].isalnum():
                clean.append(s[j].lower())

        left = 0
        right = len(clean) - 1

        for i in range(len(clean)//2):
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
