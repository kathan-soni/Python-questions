class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split()

        if words:
            return len(words[-1])
        else:
            return 0
solution = Solution()
print(solution.lengthOfLastWord("hello word"))
        