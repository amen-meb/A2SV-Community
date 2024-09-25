class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = s[i:i+2]
                result.append(chr(int(num) + 96)) 
                i += 3 
            else:
                # Single digit case
                result.append(chr(int(s[i]) + 96))  
                i += 1  
        
        return ''.join(result)
