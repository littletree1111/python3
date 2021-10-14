# leetcode 61, rotate list
# solution code from https://walkccc.me/LeetCode/problems/0061/?h=rotate+list
# time O(n), space O(1)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
          return head

        # turn linked list into circular list
        # count the length of linked list
        tail = head
        length = 1
        while tail.next:
          tail = tail.next
          length += 1
        tail.next = head  # circle the list

        
        t = length - k % length
        for _ in range(t):
          tail = tail.next
        newHead = tail.next
        tail.next = None

        return newHead