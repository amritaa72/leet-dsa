class Solution:
    def isHappy(self, n: int) -> bool:

        digits = [int(d) for d in str(n)]
        seen = set()

        while n != 1:

            if n in seen:
                return False

            seen.add(n)

            sqd = [d**2 for d in digits]
            total = sum(sqd)

            n = total
            digits = [int(d) for d in str(n)]

        return True
