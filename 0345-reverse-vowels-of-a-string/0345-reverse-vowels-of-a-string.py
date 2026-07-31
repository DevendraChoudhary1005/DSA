class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        char = list(s)

        n = len(s)
        l = 0
        r = n-1

        while l<r:
            while l<r and char[l]  not in vowels:
                l += 1
            while l<r and char[r]  not in vowels:
                r -= 1

            char[l], char[r] = char[r], char[l]
            l += 1
            r -= 1

        return "".join(char)
        
        