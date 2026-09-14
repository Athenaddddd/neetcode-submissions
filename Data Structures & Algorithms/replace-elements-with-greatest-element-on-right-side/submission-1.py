class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currmax = -1

        for i in range(len(arr)-1,-1,-1):
            origval = arr[i]
            arr[i] = currmax
            currmax = max(currmax,origval)

        return arr
