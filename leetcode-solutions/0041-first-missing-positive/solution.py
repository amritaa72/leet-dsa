class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums=sorted(set(nums))
        smallest =1
        
        for num in nums:
            if num == smallest:
                smallest+=1
        return smallest
