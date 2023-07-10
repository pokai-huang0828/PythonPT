nums = [-4, -1, 0, 3, 10]
# in this case, we can use two pointers to solve this problem, which can reduce the time complexity to O(n), and the space complexity is O(1)
# First, we can use two pointers to find the first positive number in the array, and then we can use two pointers to find the smallest number in the array
left, right = 0, len(nums) - 1
square = [0] * len(nums)

for i in range(len(nums) - 1, -1, -1):
    if nums[left] ** 2 > nums[right] ** 2:
        square[i] = nums[left] ** 2
        left += 1
    else:
        square[i] = nums[right] ** 2
        right -= 1


print(square)

