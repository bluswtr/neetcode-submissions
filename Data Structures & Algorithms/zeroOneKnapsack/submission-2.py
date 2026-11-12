class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [0 for _ in range(M + 1)]

        for c in range(M + 1): 
            if weight[0] <= c:
                dp[c] = profit[0]

        for i in range(1, N):
            for c in range(M, 1, -1):
                skip = dp[c]
                include = 0

                if c - weight[i] >= 0:
                    include = profit[i] + dp[c-weight[i]]

                dp[c] = max(skip,include)
            
        return dp[M]

