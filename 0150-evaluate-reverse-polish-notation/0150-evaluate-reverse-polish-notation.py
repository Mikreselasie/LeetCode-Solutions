class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+","-","/","*"}

        for token in tokens:
            if token in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == "+":
                    stack.append(str(num1 + num2))
                elif token == "-":
                    stack.append(str(num1 - num2))
                elif token == "*":
                    stack.append(str(num1 * num2))
                elif token == "/":
                    if num1/num2 > 0:
                        stack.append(str(floor(num1/num2)))
                    else:
                        stack.append(str(ceil(num1/num2)))
            else:
                stack.append(token)
        return int(stack[0])