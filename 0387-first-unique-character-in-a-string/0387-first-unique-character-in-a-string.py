class Solution:
    def firstUniqChar(self, s: str) -> int:
        #using dict
        freq={}#empty dict
        for ch in s:#freq count of each char
            freq[ch]=freq.get(ch,0)+1
        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1
