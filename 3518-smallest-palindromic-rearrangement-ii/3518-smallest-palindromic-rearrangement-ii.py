import collections

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)
        
        odd_count = sum(1 for c, freq in count.items() if freq % 2 == 1)
        if odd_count > 1:
            return ""

        half_count = [0] * 26
        mid_letter = ""
        for char, freq in count.items():
            half_count[ord(char) - ord('a')] = freq // 2
            if freq % 2 == 1:
                mid_letter = char

        MAX_K = k + 1

        def nCr(n, r):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res >= MAX_K:
                    return MAX_K
            return res

        def count_arrangements(counts):
            total = sum(counts)
            res = 1
            for freq in counts:
                res *= nCr(total, freq)
                if res >= MAX_K:
                    return MAX_K
                total -= freq
            return res

        if count_arrangements(half_count) < k:
            return ""

        left_half = []
        total_chars = sum(half_count)

        for _ in range(total_chars):
            for i in range(26):
                if half_count[i] == 0:
                    continue

                half_count[i] -= 1
                arrangements = count_arrangements(half_count)

                if arrangements >= k:
                    left_half.append(chr(i + ord('a')))
                    break
                else:
                    k -= arrangements
                    half_count[i] += 1

        left_str = "".join(left_half)
        return left_str + mid_letter + left_str[::-1]
        