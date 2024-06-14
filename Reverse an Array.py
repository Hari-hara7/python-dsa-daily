def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# Test the function
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
print("Reversed array:", reverse_array(arr))
