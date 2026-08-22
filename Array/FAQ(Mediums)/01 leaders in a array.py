nums = [4,9,10,5,3,-1]
ans = []
# Brute Force
for i in range(len(nums)):
    leader = True
    for j in range(i+1, len(nums)):
        if nums[j] > nums[i]:
            leader = False
            break
    if leader == True:
        ans.append(nums[i])
print(ans)


# Optimal Solution
ans1 = []
maxm = float("-inf")
for i in range(len(nums)-1, -1, -1):
    if nums[i] > maxm:
        maxm = nums[i]
        ans1.append(nums[i])

ans1.reverse()
print(ans1)

