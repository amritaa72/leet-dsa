class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p)>len(s):
            return []
        from collections import Counter
        p_count=Counter(p)
        window=Counter(s[:len(p)])

        indices=[]

        if window==p_count:
            indices.append(0)
        for i in range(len(p),len(s)):
            window[s[i-len(p)]]-=1
            if window[s[i-len(p)]]==0:
                del window[s[i-len(p)]]
            window[s[i]]+=1

            if window==p_count:
                indices.append(i-len(p)+1)
        return indices
