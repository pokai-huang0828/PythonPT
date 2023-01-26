'''
    https://leetcode.com/problems/max-consecutive-ones/description/
    485. Max Consecutive Ones
        Given a binary array nums, return the maximum number of consecutive 1's in the array.

    Example 1:

    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
    Example 2:

    Input: nums = [1,0,1,1,0,1]
    Output: 2
    

    Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
'''
def findMaxConsecutiveOnes(nums: list[int]) -> int:
    # Initialize variables to store the maximum consecutive ones found so far and the current count of consecutive ones
    maxCon, count = 0, 0
    # Iterate through the list of numbers
    for i in range(len(nums)):
        # If the current number is 1
        if nums[i] == 1:
            # Increment the count of consecutive ones
            count += 1
            # Update the maximum consecutive ones found so far
            maxCon = max(maxCon, count)
        # If the current number is not 1
        else:
            # Reset the count of consecutive ones
            count = 0
    # Return the maximum consecutive ones found
    return maxCon

# Test the function with an example list
test_array = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(test_array))

