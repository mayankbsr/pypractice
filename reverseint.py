class Solution(object):
    def string_reverse(self, s):
        r = ''
        for i in range (len(s)):
            #print (i, s[len(s) - i -1])
            r += s[len(s) - i -1]
        return r

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        out = 0
        if x > 0:
            r = self.string_reverse(str(x))
            out = int(r)
        elif x < 0:
            r = self.string_reverse(str(x)[1:])
            #print ("r", r)
            out = int(r)
            out = -1 * out
        else:
            out = 0
        
        if out > (2**31 - 1) or out < (-2**31):
            out = 0

        #print (r)
        #print (out)
        
        return out
