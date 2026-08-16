class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count0 = count1 = count2 = 0
        for val in stones:
            if (typ := val % 3) == 0:
                count0 += 1
            elif typ == 1:
                count1 += 1
            else:
                count2 += 1
        if count0 % 2 == 0:
            return count1 >= 1 and count2 >= 1
        return count1 - count2 > 2 or count2 - count1 > 2