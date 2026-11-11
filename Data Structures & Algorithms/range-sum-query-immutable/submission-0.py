class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        self.sums[0] = nums[0]
        
        for n in range(1,len(nums)):
            self.sums[n] = nums[n] + self.sums[n-1]
            # 1,2,3,4,5
            # 1,3,6,10,15

        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.sums[right] - self.sums[left-1]
        elif left == 0:
            return self.sums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)