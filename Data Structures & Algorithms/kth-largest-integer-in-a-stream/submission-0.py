import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.heap.append(-num)
        
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        newVal = -val
        heapq.heappush(self.heap, newVal)
        larger = []
        for i in range(self.k-1):
            poped = heapq.heappop(self.heap)
            larger.append(poped)
        
        kmax = -self.heap[0]
        
        for item in larger:
            heapq.heappush(self.heap, item)

        return kmax

        
