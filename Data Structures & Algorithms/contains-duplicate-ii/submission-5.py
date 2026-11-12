class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)

        for i in range(0,l): # l = 4, i = 2
            hash = {} # {2:1}
            for j in range(i,i+k): # 2 - 3, j = 3
                if j >= l:
                    break
                if nums[j] in hash:
                    return True
                hash[j] = nums[j]
        return False                                                                        
                