class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(x)[::-1]) if x > 0 else (int(str(abs(x))[::-1]) * -1)
        return 0 if (result > 2147483647 or result < -2147483647) else result

"""
https://leetcode.com/problems/reverse-integer/submissions/
Runtime: 30 ms, faster than 80.45% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.3 MB, less than 46.15% of Python3 online submissions for Reverse Integer.
"""
