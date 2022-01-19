class Solution:
    def myAtoi(self, s: str) -> int:
        result_str  = ''
        get_signed = True
        start_blank = True
        for i in s:
            if i == "-" or i == "+":
                if get_signed:
                    result_str+=i
                    get_signed = False
                    start_blank = False
                else:
                    break
            elif i == " ":
                if start_blank:
                    continue
                else:
                    break
            elif i in "0123456789":
                result_str+=i
                start_blank = False
                get_signed = False
            else:
                break
        result_int = 0
        sign = 1
        for i in result_str:
            if i == "-":
                sign = -1
            elif i == "+":
                sign = 1
            else:
                result_int = 10*result_int + int(i)
        result_int = result_int * sign
        if result_int < - 2**31:
            result_int = - 2**31
        if result_int > 2**31 -1:
            result_int = 2**31 -1
        return result_int

"""
https://leetcode.com/problems/string-to-integer-atoi/submissions/
Runtime: 52 ms, faster than 33.38% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.2 MB, less than 81.03% of Python3 online submissions for String to Integer (atoi).
"""