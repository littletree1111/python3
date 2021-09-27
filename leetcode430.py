# leetcode 430. Flatten a multilevel doubly linked list

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
	def flatten(self, head: 'Node') -> 'Node':
		# recursive solution

		# def flatten(head: 'Node', rest: 'Node') -> 'Node':
		# 	if not head:
		# 		return rest

		# 	head.next = flatten(head.child, flatten(head.next, rest))
		# 	if head.next:
		# 		head.next.prev = head
		# 	head.child = None

		# 	return head

		# return flatten(head, None)



		# iterative solution

		curr = head
		''' 
		move through each node and check if children node is present
		child node gets linked as the next node of the current
		current node gets linked as the previous node of the child node
		remove reference to child node setting curr.child to None
		last node of child node's linked list gets linked as the previous node
		of original current.next node
		tail of child node gets linked as the previous node of original
		current.next

		'''
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

