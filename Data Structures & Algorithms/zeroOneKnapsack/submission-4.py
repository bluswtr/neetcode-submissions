class Solution:
    # brute force solution
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfsHelper(0, profit, weight, capacity)

    def dfsHelper(self, i, profit, weight, capacity):
        # base case, if we reach the end
        if i == len(profit):
            return 0

        # skip item i
        maxProfit = self.dfsHelper(i + 1, profit, weight, capacity)

        # include item i
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfsHelper(i + 1, profit, weight, newCap)
            maxProfit = max(p,maxProfit)

        return maxProfit