class Solution(object):
    def isPalindrome(self, x):
        total = 0
        temp = x

        while temp > 0:
            num = temp % 10
            total = total * 10 + num
            temp = temp // 10

        return x == total
x = 121
sol = Solution()
print(sol.isPalindrome(x))