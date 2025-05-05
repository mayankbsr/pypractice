class Solution(object):
    def findShortestString(self, strs):
        shortestlen = len(strs[0])
        shortest = strs[0]
        for s in strs:
            if len(s) < shortestlen:
                shortestlen = len(s)
                shortest = s
        return shortest

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = self.findShortestString(strs)
        print ("Shortest, len", shortest, len(shortest))
        longest = ""
        for i in range(len(shortest)):
            print ("shortest", shortest[i])
            found = False
            for j in range(len(strs)):
                char = strs[j][i]   
                print ("s", char)
                if shortest[i] == char:
                    found = True
                else: 
                    found = False
                    break
            print (found)
            if found == True:
                longest = longest + char
            else:
                print("breaking")
                break
            print ("longest", longest)
        
        print (longest)
        return longest
