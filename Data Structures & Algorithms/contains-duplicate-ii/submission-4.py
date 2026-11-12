class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)

        for i in range(0,l): # l = 4, i = 0
            hash = {} # reset
            for j in range(i,i+k): # 0 - 3
                if j > l-1:
                    break
                if nums[j] in hash:
                    return True
                hash[j] = nums[j]
        return False                                                                        
                