# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        if not head:
            return None
        current_node = head
        explored_node = {}
        while True:
            explored_node[hash(current_node)] = index
            if current_node.next == None:
                return None
            try:
                a = explored_node[hash(current_node.next)]#the reason of using hash is python dictionary would expore whether a loop inside key index
                return current_node.next
            except:
                index  = index+1
                current_node = current_node.next
"""
https://leetcode.com/problems/linked-list-cycle-ii/submissions/
Runtime: 44 ms, faster than 95.74% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.4 MB, less than 18.31% of Python3 online submissions for Linked List Cycle II.
"""