import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newstones = []
        for stone in stones:
            newstones.append(-stone)
        heapq.heapify(newstones)

        while len(newstones) > 1:
            heavy1 = heapq.heappop(newstones)
            heavy2 = heapq.heappop(newstones)

            if heavy1 == heavy2:
                continue
            else:
                new = -abs(max(heavy1,heavy2) - min(heavy1,heavy2))
                heapq.heappush(newstones, new)
            
        if len(newstones) < 1:
            return 0
        else:
            ans = newstones[0]
            return -ans

                
