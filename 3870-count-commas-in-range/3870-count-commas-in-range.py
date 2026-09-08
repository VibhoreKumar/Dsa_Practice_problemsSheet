class Solution:
    def countCommas(self, n: int) -> int:
        res=0
        for i in range(1,n+1):
            if i>999:
                res+=1
        return res