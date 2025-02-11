class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return (int(y + x) - int(x + y))

# Convert all numbers to strings and sort using the custom comparator
        sorted_nums = sorted(map(str, nums), key=cmp_to_key(compare))

        # Join the sorted list and handle leading zeros
        result = ''.join(sorted_nums).lstrip('0') or '0'
        return result