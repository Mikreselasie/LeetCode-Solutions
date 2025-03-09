class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0

        for i in range(len(s)):
            temp = 0
            if s[i] == ')':
                while stack and stack[-1] != "(":
                    temp += stack[-1]
                    stack.pop()
                count = temp*2 if temp > 0 else 1
                stack.pop()
                stack.append(count)
            else:
                stack.append(s[i])
            
        return sum(stack)

            