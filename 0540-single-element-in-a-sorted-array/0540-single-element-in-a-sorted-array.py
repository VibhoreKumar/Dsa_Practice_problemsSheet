class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            # Find midpoint and round down to an even index
            mid = 2 * ((lo + hi) // 4)

            if nums[mid] == nums[mid + 1]:
                lo = mid + 2  # Single element is after this pair
            else:
                hi = mid      # Single element is at mid or before

        return nums[lo]