class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        str_x = str(x)
        start = 0
        end = len(str_x) - 1
        while start < end:
            if str_x[start] != str_x[end]:
                return False
            else:

                start +=1
                end -=1
        return True

solution = Solution()
x = int(input("enter the number : "))
result = solution.isPalindrome(x)
print(result)
        
