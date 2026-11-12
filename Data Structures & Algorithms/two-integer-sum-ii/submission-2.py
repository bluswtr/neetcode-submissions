class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        # target = 9
        # [1,2,2,3,4,6,7,10,12]
        #  l           r        

        while l < r:
            if numbers[l] + numbers[r] > target:
                if numbers[r] >= target:
                    r -= 1
                else:
                    l += 1
            elif numbers[l] + numbers[r] == target:
                return [l+1,r+1]