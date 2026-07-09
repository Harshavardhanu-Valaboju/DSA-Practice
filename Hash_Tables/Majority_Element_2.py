"""
Problem: Majority Element 2
Platform: LeetCode
Difficulty: Medium 
Topics: Array, Hash Table, Sorting, Counting

"""

def majorityElement( nums):
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    l=[]
    for i in d:
        if d[i] > len(nums)//3:
            l.append(i)
    return l
    
nums=list(map(int,input().split()))
print(majorityElement(nums))
        

"""
Time Complexity: O(n)
Space Complexity: O(n)

I have solve this problem in a very optimized manner using the dictionary 
but it has to be optimized in the space .

"""