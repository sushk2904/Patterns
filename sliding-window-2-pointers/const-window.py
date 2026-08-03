#Largest subarray of n consecutive elements with maxsum
nums = [-1, 2, 3, 3, 4, 5, -1]
k = 4
n = len(nums)
if n < k:
    print(None)
l, r = 0, k
current_sum = 0
for i in range(k):
    current_sum+=nums[i]

maxm = current_sum # This helps us having the current sum stored because this can be the highest sum and highest we have found till now so its important to declare it as the maxm sum

while r < n: # for r in range(k,n): and remove that r+=1 from below it will work with for loop too
    current_sum = current_sum - (nums[l]) + nums[r]
    l+=1
    r+=1
    maxm = max(maxm, current_sum)
print(maxm)