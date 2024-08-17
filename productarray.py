#Find the maximum product of two integers in an array where all elements are positive.

#Example

#arr = [1, 7, 3, 4, 9, 5] 
#max_product(arr) # Output: 63 (9*7)


arr = [1, 7, 3, 4, 9, 5] 
def max_product(arr):
    largest=max(arr[0],arr[1])
    second_largest=min(arr[0],arr[1])
    for i in range(2,len(arr)):
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
        elif arr[i]>second_largest:
            second_largest=arr[i]
    return largest*second_largest