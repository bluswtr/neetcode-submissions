class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum, l = 0, 0
        minLen = float("inf")

        for r in range(len(nums)): 
            currSum += nums[r] # 14
            while currSum >= target:
                minLen = min(r - l +1, minLen) # 3
                currSum -= nums[l] # 6
                l += 1

        return 0 if minLen == float("inf") else minLen
