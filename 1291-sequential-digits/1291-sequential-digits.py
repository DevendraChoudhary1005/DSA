class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample_num = "123456789"
        result = []

        low_len = len(str(low))
        high_len = len(str(high))

        for i in range(low_len, high_len + 1):
            for start in range(10 - i):
                substring = sample_num[start : start + i]
                num = int(substring)

                if low <= num <= high:
                    result.append(num)

        return result