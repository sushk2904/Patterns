class Solution:
    def reverse(self, nums, right, left):
        while right > left:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

    def rotate(self, nums, k):
        n = len(nums)
        self.reverse(nums, n-1, n-k-1)
        self.reverse(nums, n-k-1, n-1)
        self.reverse(nums, 0, n-1)
    
        