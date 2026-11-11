class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = ''.join(filter(str.isalnum,s))
        newStr = newStr.lower()
        print(newStr)
        l = 0
        r = len(newStr) - 1

        while l < r:
            if newStr[l] != newStr[r]:
                return False
            else:
                l += 1
                r -= 1
        return True