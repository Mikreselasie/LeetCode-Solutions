class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        new_matrix = []
        width = len(img[0])
        height = len(img)
        if height == 1 and width == 1:
            return img
        elif height == 1:
            temp_row = []
            for i in range(width):
                if i == 0:
                    temp_row.append((img[0][0] + img[0][1])//2)
                elif i== width-1:
                    temp_row.append((img[0][i] + img[0][i-1])//2)
                else:
                    temp_row.append((img[0][i] + img[0][i-1] + img[0][i+1])//3)
            return [temp_row]
        elif width == 1:
            temp_row = []
            for i in range(height):
                if i== 0:
                    temp_row.append([(img[0][0] + img[1][0])//2])
                elif i == height-1:
                    temp_row.append([(img[i][0] + img[i-1][0])//2])
                else:
                    temp_row.append([(img[i][0] + img[i-1][0] + img[i+1][0])//3])
            return temp_row
        else:
            for rn in range(height):
                temp_row = []
                smooth = 0
                for cn in range(width):
                    if rn == 0 and cn == 0:
                        smooth = (img[rn][cn] + img[rn+1][cn+1] + img[rn][cn+1] + img[rn+1][cn])//4
                        temp_row.append(smooth)
                    elif rn == 0 and cn == width-1:
                        smooth = (img[rn][cn] + img[rn+1][cn-1] + img[rn][cn-1] + img[rn+1][cn])//4
                        temp_row.append(smooth)
                    elif rn == height-1 and cn == 0:
                        smooth = (img[rn][cn] + img[rn-1][cn+1] + img[rn][cn+1] + img[rn-1][cn])//4
                        temp_row.append(smooth)
                    elif rn == height-1 and cn == width-1:
                        smooth = (img[rn][cn] + img[rn-1][cn-1] + img[rn][cn-1] + img[rn-1][cn])//4
                        temp_row.append(smooth)
                    elif rn  == 0:
                        smooth = (img[rn][cn] + img[rn+1][cn+1] + img[rn][cn+1] + img[rn+1][cn] + img[rn][cn-1] + img[rn+1][cn-1])//6
                        temp_row.append(smooth)
                    elif rn  == height-1:
                        smooth = (img[rn][cn] + img[rn-1][cn+1] + img[rn][cn+1] + img[rn-1][cn] + img[rn][cn-1] + img[rn-1][cn-1])//6
                        temp_row.append(smooth)
                    elif cn == 0:
                        smooth = (img[rn][cn] + img[rn+1][cn+1] + img[rn][cn+1] + img[rn+1][cn] + img[rn-1][cn] + img[rn-1][cn+1])//6
                        temp_row.append(smooth)
                    elif cn  == width-1:
                        smooth = (img[rn][cn] + img[rn+1][cn-1] + img[rn][cn-1] + img[rn+1][cn] + img[rn-1][cn] + img[rn-1][cn-1])//6
                        temp_row.append(smooth)
                    else:
                        smooth = (img[rn][cn] + img[rn+1][cn-1] + img[rn][cn-1] + img[rn+1][cn] + img[rn-1][cn] + img[rn-1][cn-1] + img[rn][cn+1] + img[rn+1][cn+1] + img[rn-1][cn+1])//9
                        temp_row.append(smooth)
                new_matrix.append(temp_row)
            return new_matrix