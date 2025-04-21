class Solution(object):
    def reverse(self, s):
        r = ''
        for i in range(len(s)):
            r += s[len(s) - i - 1]
        return r
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #return True if (str(x) == self.reverse(str(x))) else False
        y = x
        z = 0
        while y > 0:
            #print (y, y%10)
            z = z*10 + y%10
            #print (z)
            y = y//10

        return x == z

s = Solution()
print(s.isPalindrome(1234321))
