class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        count2 = {}

        for char in t:
            count2[char] = count2.get(char, 0) + 1

        return count == count2         

        



