class Solution:
	def flatten(self, head: 'Node') -> 'Node':
		# def flatten(head: 'Node', rest: 'Node') -> 'Node':
		# 	if not head:
		# 		return rest

		# 	head.next = flatten(head.child, flatten(head.next, rest))
		# 	if head.next:
		# 		head.next.prev = head
		# 	head.child = None

		# 	return head

		# return flatten(head, None)


		curr = head

		while curr:
			if curr.child:
				cachedNext = curr.next
				curr.next = curr.child
				curr.child.prev = curr
				curr.child = None
				tail = curr.next
				while tail.next:
					tail = tail.next
				tail.next = cachedNext
				if cachedNext:
					cachedNext.prev = tail
			curr = curr.next

		return head
