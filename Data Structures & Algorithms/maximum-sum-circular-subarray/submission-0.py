class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = minSum = nums[0]
        currMax = currMin = total = 0

        for num in nums: # 4
            total += num # 9
            currMin = min(currMin+num,num) # 4 
            currMax = max(currMax+num,num) # 13

            minSum = min(currMin,minSum) # -6
            maxSum = max(currMax,maxSum) # 13

        if maxSum < 0:
            return maxSum
        return max(total - minSum,maxSum)
