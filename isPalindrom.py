class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        original = x
        result = 0
        
        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x //= 10
        
        return result == original
