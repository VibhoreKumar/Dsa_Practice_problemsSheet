class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n, count=len(nums), 0
        freq=defaultdict(int)
        l=0
        for r, x in enumerate(nums):
            freq[x]+=1
            while freq[x]>k:
                freq[nums[l]]-=1
                l+=1
            count=max(count, r-l+1)
        return count