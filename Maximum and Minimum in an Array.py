def find_max_min(arr):
    if len(arr) == 0:
        return None, None  # If array is empty
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

# Test the function
arr = [1, 2, 3, 4, 5]
max_val, min_val = find_max_min(arr)
print("Array:", arr)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
