class Solution:

    def encode(self, strs: List[str]) -> str:
        # first 3 letters is number of strings
        # followed by "array" of lengths of each string each 3 letters long
        # rest is the list of strings

        # edge cases: 0, should return 000
        num = str(len(strs)).zfill(3)
        lengths = ""
        strings = ""
        
        for s in strs:
            lengths += str(len(s)).zfill(3)
            strings += s

        return (num + lengths + strings)

    def decode(self, s: str) -> List[str]:
        # read first 3 letters, get number of strings
        # read num * 3 chars to array
        # iterate through new array and store corresponding strings to array

        strings = []
        num = int(s[0:3],10)
        lengths = []
        
        print(s)
        print(num)
        for i in range(3,(num+1)*3,3):
            lengths.append(int(s[i:i+3],10))

        print(lengths)
        curr = i+3
        for l in lengths:
            strings.append(s[curr:curr+l])
            curr += l

        return strings