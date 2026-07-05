class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        def solve(index, subset):
            if index>=len(digits):
                result.append("".join(subset))
                return

            for char in char_map[digits[index]]:
                subset.append(char)
                solve(index+1, subset)
                subset.pop()

        solve(0, [])
        return result