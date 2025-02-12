class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sorted_seat = sorted(seats)
        sorted_students = sorted(students)
        total = 0
        for position in range(len(students)):
            total += abs(sorted_students[position] - sorted_seat[position])
        return total




        