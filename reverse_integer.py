class Solution(object):
    def reverse(self, x):
        if -2**31> x > 2**31:
            return 0
        sign = -1 if x < 0 else 1

        x = abs(x)
        reversed_num = int(str(x)[::-1])

        reversed_num *=sign

        return reversed_num
    
solution = Solution()
x = 123
result = solution.reverse(x)
print(result)
        