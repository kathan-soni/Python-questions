class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        
        if n == 0:
            return 0
        
        p = 1 # position acts like a counter
        
        while not(n&1): # here n is from last bit and it moves the bit towards right
        # here n%1 means it is converted to bits if n gets zero loop exits
            
            n >>= 1 # here the boxes shifted to write and checking the last digit
            p += 1
            
        return p
s1 = Solution()
result = s1.getFirstSetBit(12)
print(result)