class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        temp = self.getRow(rowIndex-1)
        
        for i in range(1,rowIndex):
            x =  temp[i] + temp[i-1]
            temp[i-1] = x

        temp = [1] + temp 
        return temp