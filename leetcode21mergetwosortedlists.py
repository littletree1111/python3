class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if not l1 or not l2:
			return l1 if l1 else l2

		# keep lesser value to be current working node
		if l1.val > l2.val:
			l1, l2 = l2, l1
		l1.next = self.mergeTwoLists(l1.next, l2)

		return l1
		

		# if not l1 or not l2:
		# 	return l1 if l1 else l2

		# dummy = ListNode()
		# anchor = dummy
		# while l1 and l2:
		# 	if l1.val <= l2.val:
		# 		anchor.next = l1
		# 		l1 = l1.next
		# 	else:
		# 		anchor.next = 12
		# 		l2 = l2.next
		# 	anchor = anchor.next
		# anchor.next = l1 if l1 else l2
		# return dummy.next