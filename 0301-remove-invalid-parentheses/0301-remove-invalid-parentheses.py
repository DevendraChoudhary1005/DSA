class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string):
            balance = 0

            for ch in string:
                if ch == "(":
                    balance += 1
                elif ch == ")":
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0


        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                result.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] in ('(', ')'):
                    next_str = curr[:i] + curr[i + 1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)

        return result