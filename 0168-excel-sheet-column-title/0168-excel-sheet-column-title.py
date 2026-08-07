class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        n =  columnNumber
        while(n > 0):
            n -= 1
            curr = n % 26
            n = int(n / 26)
            ans.append(chr(curr + ord('A')))
        
        return ''.join(ans[::-1])