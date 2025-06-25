class Solution:
    def reverseWords(self, s: str) -> str:
        empty=''
        words=s.split()
        #print(words)
        for i in range(len(words)):
            if i==0:
                empty=empty+words.pop()
            else:
                empty=empty+' '+words.pop()
        #print(empty)
        self=empty
        return self
