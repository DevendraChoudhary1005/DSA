class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        pos = [i for i, ch in enumerate(s) if ch == '1']
        
        if len(pos) < k:
            return ""

        min_len = float('inf')
        for i in range(len(pos) - k + 1):
            length = pos[i + k - 1] - pos[i] + 1
            min_len = min(min_len, length)

        candidates = [
            pos[i] for i in range(len(pos) - k + 1)
            if pos[i + k - 1] - pos[i] + 1 == min_len
        ]

        for offset in range(min_len):
            if len(candidates) == 1:
                break
            min_char = min(s[start + offset] for start in candidates)
            candidates = [start for start in candidates if s[start + offset] == min_char]

        best_start = candidates[0]
        return s[best_start : best_start + min_len]

        

        