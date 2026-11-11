import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # put stones in a max heap
        # pop off the top 2
        
        while len(stones) > 1:
            heapq.heapify_max(stones)
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x > y:
                stones.append(x - y)
        if len(stones) == 1:
            return stones[0]
        return 0

        