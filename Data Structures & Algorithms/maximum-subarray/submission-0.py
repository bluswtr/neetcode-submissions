class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        currSum = 0

        for i in nums: 
            currSum = max(currSum,0)
            currSum += i
            maxSum = max(currSum,maxSum)

        return maxSum