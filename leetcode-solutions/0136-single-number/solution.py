class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        from collections import Counter
        counts=Counter(nums)
        matching=[key for key,val in counts.items() if val==1]
        return matching[0]
