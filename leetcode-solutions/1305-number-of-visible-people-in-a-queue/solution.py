class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        lis=[]
        answer=[0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            count=0
            while lis and lis[-1]<heights[i]:
                lis.pop()
                count+=1
            if lis:
                count+=1
            answer[i]=count
            lis.append(heights[i])
        return answer

                
