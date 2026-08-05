"""Generate longest subarray/all subarray with <condition>"""
#Generate all subarrays with sum <=k
nums = [2,5,1,7,10]
k = 14
n = len(nums)
left = 0
right = 0
total = 0
maxlen = 0
while right < n:
    total += nums[right]

    if total > k: #if they ask actual element to be printed use the while > k condition
        total -= nums[left]
        left+=1
    maxlen = max(maxlen, right - left + 1)
    right+=1
print(maxlen)   