class Solution:
	def setBits(self, N):
	    count = 0
	    while N:
	        if N&1:
	            count +=1
	            
	        N>>=1
	    return count
s1= Solution()
result = s1.setBits(4)
print(result)