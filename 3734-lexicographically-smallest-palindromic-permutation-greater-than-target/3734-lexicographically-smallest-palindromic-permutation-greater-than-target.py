from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        k = n // 2
        
        total_counts = Counter(s)
        odd_chars = [c for c, count in total_counts.items() if count % 2 != 0]
        
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {c: total_counts[c] // 2 for c in total_counts}

        def build_palindrome(first_half: list[str]) -> str:
            fh = "".join(first_half)
            return fh + mid_char + fh[::-1]

        prefix_valid = True
        temp_counts = half_counts.copy()
        for i in range(k):
            c = target[i]
            if temp_counts.get(c, 0) > 0:
                temp_counts[c] -= 1
            else:
                prefix_valid = False
                break
        
        if prefix_valid:
            candidate = build_palindrome(list(target[:k]))
            if candidate > target:
                return candidate

        can_match_up_to = 0
        temp_counts = half_counts.copy()
        
        for i in range(k):
            c = target[i]
            if temp_counts.get(c, 0) > 0:
                temp_counts[c] -= 1
                can_match_up_to = i + 1
            else:
                break

        for i in range(can_match_up_to, -1, -1):
            if i > k - 1:
                continue
            
            avail = half_counts.copy()
            for ch in target[:i]:
                avail[ch] -= 1
            
            best_char = None
            for code in range(ord(target[i]) + 1, ord('z') + 1):
                ch = chr(code)
                if avail.get(ch, 0) > 0:
                    best_char = ch
                    break
            
            if best_char:
                first_half = list(target[:i]) + [best_char]
                avail[best_char] -= 1
                
                for code in range(ord('a'), ord('z') + 1):
                    ch = chr(code)
                    count = avail.get(ch, 0)
                    if count > 0:
                        first_half.extend([ch] * count)
                
                return build_palindrome(first_half)

        return ""       