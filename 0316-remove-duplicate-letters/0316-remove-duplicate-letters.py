class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        stack = []
        seen = set()

        for char in s:
            count[char] -= 1

            if char in seen:
                continue

            while stack and char<stack[-1] and count[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)

        return "".join(stack)