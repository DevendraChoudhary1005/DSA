class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            current_temp = temperatures[i]

            while stack and current_temp > temperatures[stack[-1]]:
                stack_index = stack.pop()
                res[stack_index] = i-stack_index

            stack.append(i)

        return res