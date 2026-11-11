class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = end = longest =  0
        hash = {}
        
        if s != "":
            hash[ord(s[end])] = 0
            end = longest = 1

            while end < len(s):
                ordinal = ord(s[end])
                if ordinal in hash and hash[ordinal] >= begin: # if already seen, start over
                    begin = hash[ordinal] + 1
                hash[ordinal] = end # end 2 begin 2
                longest = max(end-begin+1,longest) # longest 2
                end += 1 # end 2
        
        return longest