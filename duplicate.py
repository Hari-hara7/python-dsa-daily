'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true'''



def contains_duplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

nums = [1, 2, 3, 5]
print(contains_duplicate(nums))