class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int: 
        prefix = [len(arr)]*len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                poped = stack.pop()
                prefix[poped] = i
            stack.append(i)

        suffix = [-1]*len(arr)
        stack = []
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                poped = stack.pop()
                suffix[poped] = i
            stack.append(i)

        total = 0
        for i in range(len(arr)):
            total += (prefix[i]-i)*(i-suffix[i])*arr[i]
        return total % (10**9 + 7)