class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        my_sort = sorted(arr)
        answer = []

        if my_sort == arr:
            return []

        def flip_subarray(array, start, end):
            array[start:end+1] = array[start:end+1][::-1]
        
        length = len(arr)
        a = -1
        b = 0
        while arr != my_sort and b < length:
            if arr[b] == my_sort[a]:
                flip_subarray(arr,0,b)
                answer.append(b+1)
                flip_subarray(arr,0,length-1)
                answer.append(length)
                b = 0
                a -= 1
                length -= 1
            else:
                b += 1
        return answer       