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

I have solved this in a very simple way using the basic properties in python Set and Conditional statements.

"""