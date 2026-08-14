class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        right = -1
        freq = [0] * 26
        result = 0
        while right + 1 < len(s):
            right += 1
            c = s[right]
            freq[ord(c) - ord('a')] += 1
            while freq[ord(c) - ord('a')] > 2:
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result