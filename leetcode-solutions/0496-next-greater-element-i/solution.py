class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        lis=[]
        for i in nums1:
            itemindex=nums2.index(i)
            if itemindex+1==len(nums2):
                lis.append(-1)
            for j in nums2[itemindex+1:]:
                if j>i:
                    lis.append(j)
                    break
                elif nums2[itemindex+1:].index(j)<len(nums2[itemindex+1:])-1:
                    continue
                else:
                    lis.append(-1)
                

        return lis
                
