class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num

        digit_sum = sum(int(x) for x in str(num))

        return self.addDigits(digit_sum)