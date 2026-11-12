class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = end = longest =  0
        hash = {}
        
        if s != "":
            hash[ord(s[end])] = 0
            end = 1
            while end < len(s):
                if ord(s[end]) in hash: # if already seen, start over
                    begin = hash[ord(s[end])] + 1
                hash[ord(s[end])] = end
                longest = max(end-begin+1,longest)
                end += 1
        
        return longest