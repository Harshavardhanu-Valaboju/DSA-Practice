"""
Problem: Rotate Array
Platform: LeetCode
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def rotate(nums, k):
        n=len(nums)
        k%=n
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)

        return nums

    k=int(input())
    nums=list(map(int,input().split()))
    print(rotate(nums,k))

        