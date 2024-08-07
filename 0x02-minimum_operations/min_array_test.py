#!/usr/bin/python3
def min_operations_to_make_equal(arr):
    n = len(arr)
    if n <= 1:
        return 0
    
    # Count the frequency of each number
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    # Find the most frequent number
    max_freq = max(freq.values())
    
    # The minimum operations is the length of the array minus the frequency of the most common element
    return n - max_freq

# Example usage
arr = [1, 2, 3, 4, 2, 2, 3]
result = min_operations_to_make_equal(arr)
print(f"Minimum operations needed: {result}")