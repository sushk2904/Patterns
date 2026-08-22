nums = [2, 4, 5, -1, -3, -4]
pos = []
neg = []
for num in nums:
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)
n = len(nums)
for i in range(n//2):
    nums[2*i] = pos[i]
    nums[2*i+1] = neg[i]

print(nums)