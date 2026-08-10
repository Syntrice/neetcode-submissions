class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0: 
            return False

        map = {
            "(": ")",
            "{": "}",
            "[" : "]"
        }

        stack = []

        for char in s: 
            print(stack)
            print(char)
            if char in "({[":
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                bracket = stack.pop()
                if map.get(bracket) != char:
                    return False

        return len(stack) == 0
