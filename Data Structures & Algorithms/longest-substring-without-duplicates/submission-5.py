class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = end = longest =  0
        hash = {}
        
        if s != "":
            hash[s[end]] = 0
            end = 1
            while end < len(s):
                if s[end] in hash: # if already seen, start over
                    begin = hash[s[end]] + 1
                hash[s[end]] = end
                longest = max(end-begin+1,longest)
                end += 1
        
        return longest