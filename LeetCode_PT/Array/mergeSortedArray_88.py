'''
    ou are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
    
     
    
    Example 1:
    
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
    
    Example 2:
    
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].
    
    Example 3:
    
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
     
    
    Constraints:
    
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109
     
    
    Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''

import unittest

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Initialize a variable to store the index of the last element in nums1
    last_index = m + n - 1
    # Initialize a variable to store the index of the last element in nums2
    nums2_index = n - 1
    # Initialize a variable to store the index of the last element in nums1
    nums1_index = m - 1
    # While the index of the last element in nums1 is greater than or equal to 0
    # and the index of the last element in nums2 is greater than or equal to 0
    while nums1_index >= 0 and nums2_index >= 0:
        # If the value of the last element in nums1 is greater than or equal to the value of the last element in nums2
        if nums1[nums1_index] >= nums2[nums2_index]:
            # Set the value of the last element in nums1 to the value of the last element in nums1
            nums1[last_index] = nums1[nums1_index]
            # Decrement the index of the last element in nums1
            nums1_index -= 1
        else:
            # Set the value of the last element in nums1 to the value of the last element in nums2
            nums1[last_index] = nums2[nums2_index]
            # Decrement the index of the last element in nums2
            nums2_index -= 1
        # Decrement the index of the last element in nums1
        last_index -= 1
    # While the index of the last element in nums2 is greater than or equal to 0
    while nums2_index >= 0:
        # Set the value of the last element in nums1 to the value of the last element in nums2
        nums1[last_index] = nums2[nums2_index]
        # Decrement the index of the last element in nums2
        nums2_index -= 1
        # Decrement the index of the last element in nums1
        last_index -= 1

    return nums1
    
'''
    The time complexity of the above algorithm is O(m + n)O(m+n)O(m+n) as we are iterating through both arrays containing ‘m’ and ‘n’ elements respectively.
    
    The space complexity will be O(1)O(1)O(1) as we are not using any extra space.
'''

# Test Cases
num1 = [1,2,3,0,0,0]
m = 3
num2 = [2,5,6]
n = 3

print(merge(num1, m, num2, n))

class test_merge_function(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6])
        self.assertEqual(merge([1], 1, [], 0), [1])
        self.assertEqual(merge([2,3,0,0], 2, [1,5], 2), [1,2,3,5])
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)