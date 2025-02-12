class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill_sorted = sorted(skill)

        left = 0
        right = len(skill) - 1
        chemistry = 0
        temp_sum = skill_sorted[left] + skill_sorted[right]
        while left < right:
            if skill_sorted[left] + skill_sorted[right] != temp_sum:
                return -1
            chemistry += skill_sorted[left] * skill_sorted[right]
            left += 1
            right -= 1
        return chemistry   
            

        