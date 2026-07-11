"""
Problem: Integer to Roman 
Platform: LeetCode
Difficulty: Medium 
Topics: Hash Table, Math, String

"""


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1 ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"]

        ans = []

        for value, symbol in zip(values, symbols):
            while num >= value:
                ans.append(symbol)
                num -= value

        return "".join(ans)
num=int(input())
solution = Solution()   
print(solution.intToRoman(num))


"""
Time Complexity: O(1)
Space Complexity: O(1)

"""

