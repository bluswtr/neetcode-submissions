class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        h = {}
        l = 0
        k = len(nums)

        for r in range(0,len(nums)): # r=2
            if nums[r] in h: 
                k -= 1 # k = 4
            else:
                h[nums[r]] = 1 # {1:1,2:1}
                nums[l] = nums[r] # [1,]
                l += 1 # l = 1

        return k