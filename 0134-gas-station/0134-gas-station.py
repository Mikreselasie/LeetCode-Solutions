class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        # Check if the total gas is less than the total cost
        if sum(gas) < sum(cost):
            return -1
        
        # Initialize variables
        start = 0  # Potential starting point
        current_gas = 0  # Current gas balance
        
        for i in range(n):
            current_gas += gas[i] - cost[i]
            
            # If current_gas becomes negative, reset and try the next station
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        
        # If we complete the loop, return the starting point
        return start