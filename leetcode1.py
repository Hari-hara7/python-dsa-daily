def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
 
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")



#finding the target number with two numbers sum