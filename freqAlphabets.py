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
                num = int(s[i:i + 2])
                result.append(chr(num + 96))
                i += 3
            else:
                num = int(s[i])
                result.append(chr(num + 96))
                i += 1
        return ''.join(result)
        
