"""
Problem: Majority Element 2
Platform: LeetCode
Difficulty: Medium 
Topics: Array, Hash Table, Sorting, Counting

"""

def majorityElement( nums: List[int]) -> List[int]:
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
        