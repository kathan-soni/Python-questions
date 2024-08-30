class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        if m == n:
            return -1 
        XOR_num = m^n
        p = 1
        while XOR_num>0:
            if XOR_num&1:
                return p
            XOR_num>>=1
            p +=1
        return -1
s1 = Solution()
result = s1.posOfRightMostDiffBit(11,9)
print(result)