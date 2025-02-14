class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_left = 0
        left_right = k-1
        right_right = len(cardPoints) - 1
        right_left = len(cardPoints) - k

        left_sum = sum(cardPoints[:k])
        right_sum = sum(cardPoints[right_left:])

        count = 0
        total = 0
        while count<k:
            if left_sum > right_sum :
                total += cardPoints[left_left]
                left_sum -= cardPoints[left_left]
                left_left += 1
                right_sum -= cardPoints[right_left]
                right_left += 1
            else:
                total += cardPoints[right_right]
                right_sum -= cardPoints[right_right]
                right_right -= 1
                left_sum -= cardPoints[left_right]
                left_right -= 1
            count += 1
        return total

        