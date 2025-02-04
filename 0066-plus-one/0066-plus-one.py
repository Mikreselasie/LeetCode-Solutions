class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = "".join(map(str,digits))
        y = int(x)

        y += 1

        z = str(y)
        new_list = list(map(int,list(z)))
        return new_list
