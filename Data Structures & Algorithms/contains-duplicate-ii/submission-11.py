class Solution:
    # learned that a dictionary search is not the same as a list search in python
    # other learning, 2nd range off by 1 multiple ways ^^;;;;;
    # need to read definitions more carefully

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        # initialize
        for r in range(len(nums)): # 1
            if nums[r] in h:
                i = h[nums[r]] # 
                if r - i <= k:
                    return True
            h[nums[r]] = r # {1:0,2:1,3:1}

        return False
'''         
        l = len(nums)

        for i in range(0,l): # l = 4, i = 2
            hash = [] # {2:1}
            for j in range(i,i+k+1): # 2 - 3, j = 3
                if j >= l:
                    break
                if nums[j] in hash:
                    return True
                hash.append(nums[j])
        return False  
'''                                                                      
                