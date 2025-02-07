class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        answer = [0,0]
        for num,num_count in count.items():
            answer[0] += num_count // 2
            if num_count % 2 == 1:
                answer[1] += 1
        return answer

        