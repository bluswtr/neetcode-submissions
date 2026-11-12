class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = end = longest =  0
        hash = {}
        
        if s != "":
            hash[ord(s[end])] = 0
            end = longest = 1
            while end < len(s):
                if ord(s[end]) in hash: # if already seen, start over
                    begin = end
                hash[ord(s[end])] = end # end 2 begin 2
                longest = max(end-begin+1,longest) # longest 2
                end += 1 # end 2
        
        return longest