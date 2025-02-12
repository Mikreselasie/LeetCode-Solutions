class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = sorted(people)

        left = 0
        right = len(people) - 1
        count = 0
        while left <= right:
            if sorted_people[left] + sorted_people[right] > limit:
                count += 1
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1
        return count
            

        