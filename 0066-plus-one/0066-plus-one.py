class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = "".join(map(str, digits))

        digits_str = str(int(digits_str)+1)

        return [int(x) for x in digits_str]