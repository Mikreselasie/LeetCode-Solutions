class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = ["(","{","["]
        closers = [")","}","]"]
        for brace in s:
            if brace in openers:
                stack.append(brace)
            else:
                if stack and openers.index(stack[-1]) == closers.index(brace):
                    stack.pop()
                else:
                    return False
        return stack == []