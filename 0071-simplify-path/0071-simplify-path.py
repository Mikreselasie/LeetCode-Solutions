class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = []

        for dir in dirs:
            if dir == "" or dir == ".":
                continue
            elif dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
                
        return "/" + "/".join(stack)