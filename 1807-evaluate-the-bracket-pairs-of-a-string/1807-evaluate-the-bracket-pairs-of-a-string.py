class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        my_dict = dict(knowledge)

        res = []
        curr_key = []
        inside_bracket = False

        for ch in s:
            if ch == '(':
                inside_bracket = True
                curr_key = []
            elif ch == ')':
                inside_bracket = False
                key_str = "".join(curr_key)
                res.append(my_dict.get(key_str, "?"))
            else:
                if inside_bracket:
                    curr_key.append(ch)
                else:
                    res.append(ch)

        return "".join(res)

 