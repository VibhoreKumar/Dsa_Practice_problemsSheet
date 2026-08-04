class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        for i in range(len (s)):
            min_distance = float("inf") 
           
            for j in range(len(s)):
                if s[j] == c:
                    min_distance = min(min_distance, abs(i - j))

            res.append(min_distance)

        return res
