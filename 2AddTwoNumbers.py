# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final_result = ListNode()
        result = final_result
        extra_number = 0
        while True:
            l1  = self.checkNone(l1)
            l2  = self.checkNone(l2)
            result.val = (l1.val + l2.val + extra_number) % 10
            extra_number = (l1.val + l2.val + extra_number) // 10
            if l1.next != None or l2.next != None:
                result.next = ListNode()
                result = result.next
                l1 = l1.next
                l2 = l2.next
            else:
                break
        if extra_number != 0:
            result.next = ListNode(val =extra_number)
        return final_result
    def checkNone(self, given: Optional[ListNode]):
        if given == None:
            given = ListNode(val=0)
        return given
"""
https://leetcode.com/problems/add-two-numbers/submissions/
Runtime: 96 ms, faster than 29.31% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.3 MB, less than 72.61% of Python3 online submissions for Add Two Numbers.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_number = self.ln2number(l1)
        l2_number = self.ln2number(l2)
        result_number = l1_number+l2_number
        return self.number2ln(result_number)
        
    def ln2number(self,ln):
        result_number = 0
        lenth = 0
        while ln:
            result_number = ln.val * (10**lenth) + result_number
            ln = ln.next
            lenth += 1
        return result_number
    def number2ln(self,number):
        result_node = ListNode()
        result = result_node
        while True:
            result.val = number%10
            number = number//10
            if number != 0:
                result.next = ListNode()
                result = result.next
            else:
                break
        return result_node
"""
Runtime: 119 ms, faster than 13.23% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.4 MB, less than 45.00% of Python3 online submissions for Add Two Numbers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
f = open("user.out", "w")
lines = __Utils__().read_lines()
trash = {91: None, 93: None, 44: None, 10: None}
while True:
    try:
        param_1 = int(next(lines).translate(trash)[::-1])
        param_2 = int(next(lines).translate(trash)[::-1])
        f.writelines(("[", ",".join(str(param_1 + param_2))[::-1], "]\n"))
    except StopIteration: exit()
"""
btw, this is the solution of fastest, as we can see, he is just cheating.
"""