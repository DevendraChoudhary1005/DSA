class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        pref = [(0, 0, 0)]
        
        for char in s:
            d = ord(char) - ord('0')
            prev_sum, prev_count, prev_val = pref[-1]
            
            if d > 0:
                pref.append((prev_sum + d, prev_count + 1, (prev_val * 10 + d) % MOD))
            else:
                pref.append((prev_sum, prev_count, prev_val))
        
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []
        for l, r in queries:
            sum_r, count_r, val_r = pref[r + 1]
            sum_l, count_l, val_l = pref[l]
            
            n0 = count_r - count_l
            digit_sum = sum_r - sum_l
            
            x = (val_r - val_l * pow10[n0]) % MOD
            ans.append((x * digit_sum) % MOD)
            
        return ans