class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        c = 0

        for word in words:

            if any(ch.isdigit() for ch in word):
                continue

            if word.count('-') > 1:
                continue

            if word.startswith('-') or word.endswith('-'):
                continue

            if word.count('!') + word.count('.') + word.count(',') > 1:
                continue

            if any(ch in '!.,' for ch in word[:-1]):
                continue

            if '-' in word:
                i = word.index('-')
                if not (word[i-1].islower() and word[i+1].islower()):
                    continue

            c += 1

        return c
