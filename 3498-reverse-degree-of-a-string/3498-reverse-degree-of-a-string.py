class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        basic_ascii = ord('a')
        index = 1

        for char in s:
            char_value = 26 - (ord(char) - basic_ascii)

            total += (char_value * index)
            index += 1

        return total