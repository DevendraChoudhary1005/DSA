class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_len = 0
        total_fruits = {}

        for right in range(len(fruits)):
            current_fruit = fruits[right]
            total_fruits[current_fruit] = total_fruits.get(current_fruit, 0) + 1

            while len(total_fruits) > 2:
                left_fruit = fruits[left]
                total_fruits[left_fruit] -= 1

                if total_fruits[left_fruit] == 0:
                    del total_fruits[left_fruit]

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len 