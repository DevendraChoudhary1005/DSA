class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)

        for i in range(0, n):
            charset = set()
            for j in range(i, n):
                if s[j] in charset:
                    break
                max_len = max(max_len, j-i+1)
                charset.add(s[j])

        return max_len
        