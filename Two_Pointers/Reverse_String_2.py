"""
Problem: Reverse String 2
Platform: LeetCode
Difficulty: Easy 
Topics: Two Pointers, Mid Level, String

"""


def reverseStr( s: str, k: int) -> str:
    s=list(s)
    n=len(s)
    for i in range(0,n,2*k):
        left=i
        right=min(i+k-1,n-1)
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
            
    return "".join(s)

s=input()
k=int(input())
print(reverseStr(s,k))




"""
Time Complexity: O(n)
Space Complexity: O(n)

I solved this problem using the Two pointers approach .

"""