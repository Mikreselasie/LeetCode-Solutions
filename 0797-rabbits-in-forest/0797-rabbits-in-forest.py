class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counted = Counter(answers)
        total = 0
        for answer, count in counted.items():
            group_size = answer + 1
            num_groups = (count + group_size - 1) // group_size
            total += num_groups * group_size
        
        return total