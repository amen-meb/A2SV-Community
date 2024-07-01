class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        char_set_dict = {}
    
        for word in words:
            char_set = ''.join(sorted(set(word)))
            if char_set in char_set_dict:
                char_set_dict[char_set] += 1
            else:
                char_set_dict[char_set] = 1
    
        count = 0
        for value in char_set_dict.values():
            if value > 1:
                count += (value * (value - 1)) // 2
    
        return count
