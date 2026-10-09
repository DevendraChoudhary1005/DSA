class Solution:
    def minInsertions(self, s: str) -> int:
        neededRight = 0
        missingLeft = 0
        missingRight = 0

        for c in s:
            if c == '(':
                # If neededRight is odd, we are splitting an expected pair, 
                # so insert 1 right parenthesis first.
                if neededRight % 2 == 1:
                    missingRight += 1
                    neededRight -= 1
                neededRight += 2
            else:  # c == ')'
                neededRight -= 1
                # If neededRight drops below 0, we have an extra closing bracket,
                # so we must insert 1 left parenthesis.
                if neededRight < 0:
                    missingLeft += 1
                    neededRight += 2

        return neededRight + missingLeft + missingRight    