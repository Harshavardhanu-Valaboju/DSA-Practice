"""
Problem: Contains Duplicate
Platform: LeetCode
Difficulty: Easy 
Topics: Array, Hash Table, Sorting

"""


def containsDuplicate( nums):
    a=len(nums)
    b=len(set(nums))
    if a==b:
        return False
    else:
        return True
nums=list(map(int,input().split()))
print(containsDuplicate(nums))


"""
Time Complexity: O(n)
Space Complexity: O(n)

I have solve this problem in a very optimized manner using the set and without using a Loop.

"""