class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of current length, current character,
        # number of different characters (not exceeding k)
        # length of unique chars cannot exceed k + 1
        h = {}
        t = 0 # total
        l = 0 # left
        r = 0 # replacements
        f = 0 # highest frequency, total - f = r

        for char in s: # XYYX
            t += 1 # t = 4
            if char in h: 
                h[char] += 1 # {X:2,Y:2}
            else:
                h[char] = 1
            
            f = max(h[char],f) # f = 2
            r = t - f # r = 2
            
            if r > k: # shrink window
                if s[l] in h:
                    h[s[l]] -= 1
                l += 1
                t -= 1

        return t