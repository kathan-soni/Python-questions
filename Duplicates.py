# from typing import List
class Solution():
    def removeDuplicate(self, arr):
        seen = set()
        duplicate = set()
        
        for i in arr:
            if i in seen:
                duplicate.add(i)
            else:
                seen.add(i)
        result = sorted(list(duplicate))
        return result if result else [-1]    
s1 = Solution()
final = s1.removeDuplicate([2,3,1,4,2])
print(final)