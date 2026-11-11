

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # put stones in a max heap
        # pop off the top 2
        
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)

        return stones[0] if stones else 0

        