class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        set_unique=set(nums)
        d={}
        n= len(nums)
        for i in set_unique:
            count = nums.count(i)
            d[count]=i
        max_1 = max(list(d))
        if max_1>(n/2):
            return d.get(max_1)
