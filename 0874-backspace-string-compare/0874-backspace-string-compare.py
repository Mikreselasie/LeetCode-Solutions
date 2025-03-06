class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for i in s:
            if i == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
        for k in t:
            if k == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(k)

        return stack1 == stack2