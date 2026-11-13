class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_tally = {}
        t_tally = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in s_tally:
                s_tally[s[i]] += 1
            else:
                s_tally[s[i]] = 1
        
        for j in range(len(t)):
            if t[j] in t_tally:
                t_tally[t[j]] += 1
            else:
                t_tally[t[j]] = 1

        for key in t_tally:
            if key in s_tally:
                if s_tally[key] != t_tally[key]:
                    return False
            else:
                return False
        
        return True
        
        