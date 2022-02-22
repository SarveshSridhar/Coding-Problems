class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n,s,i = columnTitle,0,0
        while len(n)>0:
            s = (ord(n[-1]) - ord('A') + 1)*pow(26,i) + s
            n = n[:len(n)-1]
            i += 1
        return s
