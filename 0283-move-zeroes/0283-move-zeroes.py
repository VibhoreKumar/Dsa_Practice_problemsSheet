class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #using overwrite method
        pos=0
        #first non_zero
        for num in nums:
            if num!=0:
                nums[pos]=num
                pos+=1

        #now for zeros
        while pos<len(nums):
            nums[pos]=0
            pos+=1