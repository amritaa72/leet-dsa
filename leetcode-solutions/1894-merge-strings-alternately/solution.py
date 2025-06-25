class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        empty=''

        lenw1=len(word1)
        lenw2=len(word2)

        w1=list(word1)
        w2=list(word2)

        if lenw1>lenw2:
            for i in range(lenw2):
                empty=empty+word1[i]+word2[i]
            empty=empty+word1[lenw2:]
            print(empty)
        else:
            for i in range(lenw1):
                empty=empty+word1[i]+word2[i]
            empty=empty+word2[lenw1:]
            print(empty)
        self=empty
        return self
