'''Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.'''

'''Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87'''



def first_second(my_list):
    # Initialize max1 and max2 to negative infinity
    max1, max2 = float('-inf'), float('-inf')
 
    # Iterate over each number in the list
    for num in my_list:
        if num > max1:
            # If the current number is greater than max1
            max2 = max1  # Update max2 to be the previous max1
            max1 = num   # Update max1 to be the current number
        elif num > max2 and num != max1:
            # If the current number is greater than max2 and is not equal to max1
            max2 = num   # Update max2 to be the current number
 
    return max1, max2  # Return the two largest unique numbers
 
# Example usage
my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))  # Output: (90, 87)



'''Iteration Details:

First Iteration: num = 84
84 > -inf: Yes, so max1 = 84, max2 remains -inf.
Second Iteration: num = 85
85 > 84: Yes, so max2 = 84, max1 = 85.
Third Iteration: num = 86
86 > 85: Yes, so max2 = 85, max1 = 86.
Fourth Iteration: num = 87
87 > 86: Yes, so max2 = 86, max1 = 87.
Fifth Iteration: num = 85
85 > 86: No, but 85 > 86 and 85 != 87: No, so no changes.
Sixth Iteration: num = 90
90 > 87: Yes, so max2 = 87, max1 = 90.
Further Iterations: The remaining numbers are all less than 90 and 87, so no changes occur.
Final Result:

max1 = 90
max2 = 87 '''