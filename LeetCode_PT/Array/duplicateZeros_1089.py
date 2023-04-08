'''
    Duplicate Zeros (1089)

    Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

    Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
    

    Example 1:
    
    Input: arr = [1,0,2,3,0,4,5,0]
    Output: [1,0,0,2,3,0,0,4]
    Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
    
    Example 2:
    
    Input: arr = [1,2,3]
    Output: [1,2,3]
    Explanation: After calling your function, the input array is modified to: [1,2,3]
     
    
    Constraints:
    
    1 <= arr.length <= 104
    0 <= arr[i] <= 9

'''

import unittest


def duplicateZeros(arr: list[int]) -> None:
    # Count the number of zeros in the array
    zero_count = 0
    for z in arr:
        if z == 0:
            zero_count += 1
    # Also can use the following:
    '''
    for z in arr:
        zero_count += z == 0
    '''
    # find the last index of the array
    last = len(arr)
    
    # Iterate through the array backwards
    for i in range(last -1, -1, -1):
        # If the number of zeros is greater than zero and the index of the array plus the number of zeros is less than the last index of the array
        if i + zero_count < last:
            # Store the number in the array at the index of the array plus the number of zeros
            arr[ i + zero_count ] = arr[i]
        # If the number of zeros is greater than zero and the index of the array plus the number of zeros is equal to the last index of the array
        if arr[i] == 0:
            # Decrement the number of zeros
            zero_count -= 1
            # If the index of the array plus the number of zeros is less than the last index of the array
            if zero_count + i < last:
                # Store zero in the array at the index of the array plus the number of zeros
                arr[i + zero_count] = 0
    
    # return the array
    return arr
'''
    The time complexity of this algorithm is O(n) because we iterate through the array once.
    
    The space complexity of this algorithm is O(1) because we do not create any additional data structures.
'''

# Test array
testing_array = [1,0,2,3,0,4,5,0]

print(duplicateZeros(testing_array))


# Unit Test
class duplicate_Zero_unit_test(unittest.TestCase):
    def test_duplicate_zero(self):
        unittest.TestCase.assertEqual(self, duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]), [1, 0, 0, 2, 3, 0, 0, 4])
        unittest.TestCase.assertEqual(self, duplicateZeros([1, 2, 3]), [1, 2, 3])
        # Error case
        unittest.TestCase.assertEqual(self, duplicateZeros([0, 1, 0, 3, 0, 0, 6]), [0, 0, 1, 0, 0, 3, 6])
        
if __name__ == '__main__':
    unittest.main()

    