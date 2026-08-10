class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for op in operations:
            if op == "+":
                sum += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                sum += (2 * stack[-1])
                stack.append(2 * stack[-1])
            elif op == "C":
                sum -= stack.pop()
            else:
                sum += int(op)
                stack.append(int(op))
        return sum