class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        mink = max(piles)
        left = 1
        right = max(piles)
        
        while left <= right:
            count = 0
            mid = (right - left)//2 + left

            for i in range(0,len(piles)):
                if mid >= piles[i]:
                    count = count + 1
                else:
                    if piles[i] % mid == 0:
                        count = count + piles[i]//mid
                    else:
                        count = count + piles[i]//mid + 1
            
            if count <= h:
                mink = min(mink,mid)
                right = mid - 1
            else:
                left = mid + 1
            
        return mink



