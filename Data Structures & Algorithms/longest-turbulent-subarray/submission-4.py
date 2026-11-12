class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        # [2,4,3,2,2,5,1,4]
        #  0 1 2 3 4 5 6 7
        r = 1
        l = 0
        res = 1
        prev = None

        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                res = max(res,r-l+1)
                r += 1
                prev = ">"
            elif arr[r-1] < arr[r] and prev != "<":
                res = max(res,r-l+1)
                r += 1
                prev = "<"
            else:
                r = r + 1 
                if arr[r] == arr[r - 1]:
                    l = r
                else:
                    l = r - 1
                prev = None
        return res