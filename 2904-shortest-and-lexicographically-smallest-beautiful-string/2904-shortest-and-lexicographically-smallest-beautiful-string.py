class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Collect all 0-based indices of '1's
        pos = [i for i, ch in enumerate(s) if ch == '1']
        
        if len(pos) < k:
            return ""

        # Step 1: Find the minimum length among all valid windows
        min_len = float('inf')
        for i in range(len(pos) - k + 1):
            length = pos[i + k - 1] - pos[i] + 1
            min_len = min(min_len, length)

        # Step 2: Filter start indices of candidates with length == min_len
        candidates = [
            pos[i] for i in range(len(pos) - k + 1)
            if pos[i + k - 1] - pos[i] + 1 == min_len
        ]

        # Step 3: Find the lexicographically smallest candidate
        # Compare characters column-by-column across remaining candidates in O(N)
        for offset in range(min_len):
            if len(candidates) == 1:
                break
            min_char = min(s[start + offset] for start in candidates)
            candidates = [start for start in candidates if s[start + offset] == min_char]

        best_start = candidates[0]
        return s[best_start : best_start + min_len]

        

        