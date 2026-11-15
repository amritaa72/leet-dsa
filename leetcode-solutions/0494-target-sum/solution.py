class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        #import Counter
        count=collections.Counter({0:1})
        for i in nums:
            step=collections.Counter()
            for j in count:
                step[i+j]+=count[j]
                step[j-i]+=count[j]
            count=step
        return count[target]

