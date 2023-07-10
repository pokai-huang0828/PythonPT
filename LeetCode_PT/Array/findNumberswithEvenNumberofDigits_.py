'''
    Find Numbers with Even Number of Digits
        Given an array nums of integers, return how many of them contain an even number of digits.
    
     
    
    Example 1:
    
    Input: nums = [12,345,2,6,7896]
    Output: 2
    Explanation: 
    12 contains 2 digits (even number of digits). 
    345 contains 3 digits (odd number of digits). 
    2 contains 1 digit (odd number of digits). 
    6 contains 1 digit (odd number of digits). 
    7896 contains 4 digits (even number of digits). 
    Therefore only 12 and 7896 contain an even number of digits.
    
    Example 2:
    
    Input: nums = [555,901,482,1771]
    Output: 1 
    Explanation: 
    Only 1771 contains an even number of digits.
     
    
    Constraints:

    1 <= nums.length <= 500
    1 <= nums[i] <= 105
       
       
    Hide Hint #1  
        How to compute the number of digits of a number ?
    Hide Hint #2  
        Divide the number by 10 again and again to get the number of digits.
'''

import unittest

def findNumberswitchEvenNumberofDigits(nums: list[int]) -> int:
    # Initialize a variable to store the count of numbers with even number of digits
    count = 0
    # 為了不要再for迴圈內在做一個for迴圈，所以用while迴圈來計算每個數字的位數
    for i in range(len(nums)):
        # Initialize a variable to store the number of digits in the current number
        num_digits = 0
        # 用while迴圈來計算每個數字的位數，會將每個數字除以10，直到數字小於0
        while nums[i] > 0:
            # Increment the number of digits in the current number
            num_digits += 1
            # Divide the current number by 10
            nums[i] //= 10
        # 如果除完的數字的位數最終是偶數，count就加1
        if num_digits % 2 == 0:
            # Increment the count of numbers with even number of digits
            count += 1
    # Return the count of numbers with even number of digits
    return count

# Test the function with an example list
test_array = [12,345,2,6,7896]
print("For test_array = [12, 345, 2, 6, 7896], the result is: " + str(findNumberswitchEvenNumberofDigits(test_array)))

'''
    The time complexity of the above algorithm is O(n) where n is the number of elements in the input array. Because we are iterating through the input array only once.
    
    The space complexity of the above algorithm is O(1). Because we are not using any extra space.
'''

class TestCase(unittest.TestCase):
    def test_findNumberswitchEvenNumberofDigits(self):
        self.assertEqual(findNumberswitchEvenNumberofDigits([12, 345, 2, 6, 7896]), 2)
        self.assertEqual(findNumberswitchEvenNumberofDigits([555, 901, 482, 1771]), 1)
        self.assertEqual(findNumberswitchEvenNumberofDigits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)