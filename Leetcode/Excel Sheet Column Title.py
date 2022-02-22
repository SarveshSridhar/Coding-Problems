class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        storage = ""
        while columnNumber>0:
            columnNumber -= 1
            storage += chr(columnNumber%26 + ord('A'))
            columnNumber //= 26
        return(storage[::-1])
            
            
