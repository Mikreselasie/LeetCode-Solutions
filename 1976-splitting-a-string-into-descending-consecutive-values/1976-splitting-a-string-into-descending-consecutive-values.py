class Solution:
    def splitString(self, s: str) -> bool:
        
        def split(path,i):
            if i == len(s):
                for k in range(1,len(path)):
                    if path[k] != path[k-1] - 1:
                        return False
                return len(path) >= 2

            num = 0
            for j in range(i,len(s)):
                num = num * 10 + int(s[j])
                path.append(num)
                if split(path,j + 1):
                    return True
                path.pop()
            return False
        return split([],0)