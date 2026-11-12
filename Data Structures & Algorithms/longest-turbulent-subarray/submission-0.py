class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        # [2,4,3,2,2,5,1,4]
        #  0 1 2 3 4 5 6 7
        # last 0 -> less than
        # last 1 -> greater than

        c = t = 0 # c = 0, t = 2
        last = -1 # 0


        for i in range(0,len(arr) - 1): # arr[i] = 1 
            if arr[i] < arr[i + 1]: 
                if last == -1 or last == 1: 
                    last = 0
                    c += 1
                    if i == len(arr) - 2:
                        c += 1
                    t = max(c,t)
                else: # reset
                    last = -1
                    c = 0
            elif arr[i] > arr[i + 1]:
                if last == -1 or last == 0:
                    last = 1
                    c += 1
                    if i == len(arr) - 2:
                        c += 1
                    t = max(c,t)
                    
                else:
                    last = -1
                    c = 0
            else:
                last = -1
                c = 0
        return t