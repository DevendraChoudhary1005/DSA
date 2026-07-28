class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        mid = n//2

        left_half = sorted(s[:mid])

        mid = s[mid] if n%2 == 1 else ""

        return "".join(left_half) + mid + "".join(reversed(left_half))