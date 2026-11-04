class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(x,y):
            left=0
            right=len(x)-1

            while left<right:
                if x[left]!=y[right]:
                    break
                left+=1
                right+=-1
            return((x[left:right+1]==x[left:right+1][::-1]) or (y[left:right+1]==y[left:right+1][::-1]))
        return check(a,b) or check(b,a)
