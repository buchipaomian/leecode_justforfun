class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = []
        for i in range(numRows):
            result.append("")
        index = 0
        going_down = True
        for k in s:
            result[index] += k
            if going_down:
                if index == numRows - 1:
                    going_down = False
                    index -= 1
                else:
                    index += 1
            else:
                if index == 0:
                    going_down = True
                    index += 1
                else:
                    index -= 1
        m = ""
        for r in result:
            m+=r
        return m


"""
https://leetcode.com/problems/zigzag-conversion/
Runtime: 95 ms, faster than 31.19% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 14.4 MB, less than 45.86% of Python3 online submissions for Zigzag Conversion.

I would assume this is the best solution
"""