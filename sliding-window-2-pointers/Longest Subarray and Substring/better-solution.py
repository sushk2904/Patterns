def longest_subarray_ultimate(nums, k):
    left = 0
    total = 0
    
    for right in range(len(nums)):
        total += nums[right]
        
        if total > k:
            total -= nums[left]
            left += 1
            
    # The maximum length is naturally the size of the array minus the left pointer's final position
    return len(nums) - left

nums = [2, 5, 1, 7, 10]
k = 14
print(longest_subarray_ultimate(nums, k)) 