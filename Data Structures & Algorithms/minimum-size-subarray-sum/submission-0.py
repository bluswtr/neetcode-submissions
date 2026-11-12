class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = currLen = minLen = l = r = 0

        while r < len(nums): 
            currSum += nums[r] # 14
            currLen += 1 # 5
            while currSum >= target:
                minLen = currLen # 3
                currLen -= 1 # 2
                currSum -= nums[l] # 6
                l += 1
            r += 1
        return minLen
