class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        num = len(strs)
        for col in range(len(strs[0])):
            column = ''.join([strs[row][col] for row in range(num)])
            if column != ''.join(sorted(column)):
                count += 1
        return count
