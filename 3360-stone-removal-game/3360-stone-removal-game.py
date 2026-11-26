class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        stones = 10
        turns = 0

        while n >= stones:
            n -= stones
            stones -= 1
            turns += 1

        return turns % 2 == 1