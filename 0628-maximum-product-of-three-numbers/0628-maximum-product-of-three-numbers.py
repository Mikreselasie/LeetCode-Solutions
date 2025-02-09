class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        negatives = []
        positive_and_neg = -1000000000
        positives_mult = -1000000000
        positives = []
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        negatives.sort()
        positives.sort()
        if positives and not negatives:
            positives_mult = positives[-1] * positives[-2] * positives[-3]
        if negatives and positives:
            if len(negatives) >= 2:
                positive_and_neg = negatives[0] * negatives[1] * positives[-1] 
            if len(positives) >= 3:
                positives_mult = positives[-1] * positives[-2] * positives[-3]
        elif negatives and not positives:
            positive_and_neg = negatives[-1] * negatives[-2] * negatives[-3]

        maxim = max(positives_mult,positive_and_neg)
        return maxim
        