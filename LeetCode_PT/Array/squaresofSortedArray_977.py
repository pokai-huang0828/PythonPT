'''
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 
    Example 1:
    
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
    Example 2:
    
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]
     
    
    Constraints:
    
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

'''

import unittest

# Solution 1: Two Pointer Approach
def sortedSquares_twoPointer(nums: list[int]) -> int:
    # Initialize variables to store the left and right pointers
    left, right = 0, len(nums) - 1
    # Initialize an array to store the squares of the numbers
    squares = [0] * len(nums)
    # Iterate through the array
    for i in range(len(nums) - 1, -1, -1):
        # If the absolute value of the left number is greater than the absolute value of the right number
        if abs(nums[left]) > abs(nums[right]):
            # Store the square of the left number in the array
            squares[i] = nums[left] ** 2
            # Increment the left pointer
            left += 1
        # If the absolute value of the left number is less than or equal to the absolute value of the right number
        else:
            # Store the square of the right number in the array
            squares[i] = nums[right] ** 2
            # Decrement the right pointer
            right -= 1
    # Return the array of squares
    return squares
'''
    The time complexity of this algorithm is O(n) because we iterate through the array once.
    
    The space complexity of this algorithm is O(n) because we create an array to store the squares of the numbers.
'''
    
# Solution 2: Sort Approach
def sortedSquares_Sort(nums: list[int]) -> int:
    # Iterate through the array
    for i in range(len(nums)):
        # Square each number
        nums[i] = nums[i] ** 2
    # Sort the array
    nums.sort()
    # Return the array
    return nums
    
'''
    The time complexity of this algorithm is O(nlogn) because we iterate through the array once and sort the array.
    
    The space complexity of this algorithm is O(1) because we do not create any additional data structures.
'''
    
# Solution 3: Built-in Function Approach
def sortedSquares_Built_in_function(nums: list[int]) -> int:
    # Return the sorted array of squares
    return sorted([x*x for x in nums])
    
'''
    The time complexity of this algorithm is O(nlogn) because we iterate through the array once and sort the array.
    
    The space complexity of this algorithm is O(n) because we create an array to store the squares of the numbers.
'''

# Test the function with an example list
test_list = [-4, -1, 0, 3, 10]
test_list2 = [-7, -3, 2, 6, 11]
test_list3 = [-8, -5, -3, 1, 4]
print("The squares of the numbers in the list are (Using Two Pointer): " + str(sortedSquares_twoPointer(test_list)))
print("The squares of the numbers in the list are (Using Sort Function): " + str(sortedSquares_Sort(test_list)))
print("The squares of the numbers in the list are (Using Built-in Function): " + str(sortedSquares_Built_in_function(test_list2)))

# Unit Test for the function
class Test_Squares_of_Sorted_Array(unittest.TestCase):
    def test_Squares_of_Sorted_Array(self):
        unittest.TestCase.assertEqual(self, sortedSquares_twoPointer(test_list), [0,1,9,16,100])
        # Error answer
        unittest.TestCase.assertEqual(self, sortedSquares_twoPointer(test_list2), [4,9,9,49,121]) 
        
        unittest.TestCase.assertEqual(self, sortedSquares_twoPointer(test_list3), [1,9,16,25,64])
        

if __name__ == '__main__':
    # Run the unit test, verbosity = 2 for more details, exit = False to prevent the program from exiting, argv = ['first-arg-is-ignored'] to prevent the program from reading the command line arguments
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)


        


