class Solution:
    def decodeString(self, s: str) -> str:
        idx = 0
        def helper(idx):
            stack = []
            while idx < len(s):
                if s[idx].isdigit():
                    newidx = idx
                    while idx<len(s) and s[idx].isdigit(): 
                        idx += 1

                    num = int(s[newidx:idx])
                    ans = helper(idx)
                    stack.extend(ans[0]*num)
                    idx = max(ans[1],idx)
                elif s[idx] != "[" and s[idx] != "]":
                    stack.append(s[idx])

                elif s[idx] == "]":
                    return ["".join(stack), idx]
                idx += 1
                
            return ["".join(stack), idx]
        total = []
        while idx < len(s):
            ans = helper(idx)
            idx = ans[1]+1
            total.extend(ans[0])
            
        return "".join(total)