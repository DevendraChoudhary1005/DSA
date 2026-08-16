class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """max_len = 0
        n = len(s)

        for i in range(0, n):
            charset = set()
            for j in range(i, n):
                if s[j] in charset:
                    break
                max_len = max(max_len, j-i+1)
                charset.add(s[j])

        return max_len"""

        my_dict = {}
        n = len(s)
        l = 0
        r = 0
        max_len = 0

        while r<n:
            if s[r] in my_dict:
                l = max(l, my_dict[s[r]]+1)

            max_len = max(max_len, r-l+1)
            my_dict[s[r]] = r
            r += 1

        return max_len
        