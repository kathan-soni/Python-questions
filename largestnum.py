from typing import List

class Solution:
    def largest(self, n: int, arr: List[int]) -> int:
        # Initialize the maximum element as the first element of the array
        max_element = arr[0]
        
        # Iterate through the array to find the largest element
        for num in arr:
            if num > max_element:
                max_element = num
                
        return max_element
