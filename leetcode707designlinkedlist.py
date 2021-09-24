# leetcode problem 707 design linked list
# Design a singly or a doubly linked list.

# follow along of solution from walkccc/Leetcode
# https://walkccc.me/LeetCode/problems/0707/?h=design+linked

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class MyLinkedList:
	def __init__(self):
		self.length = 0
		# self.dummy = Node(0)  # why the value 0? why not None?
		self.head = Node(0)

	def get(self, index: int) -> int:
		# return value of nth index of list
		# if index is invalid, return -1
		if index < 0 or index >= self.length:
			return -1
		# 
		# curr = self.dummy.next
		curr = self.head.next
		for _ in range(index):
			curr = curr.next
		return curr.val

	def addAtHead(self, val: int) -> None:
		temp = self.head.next
		self.head.next = Node(val)
		self.head.next.next = temp
		self.length += 1

	def addAtTail(self, val: int) -> None:
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = Node(val)
		self.length += 1

	def addAtIndex(self, index: int, val: int) -> None:
		if index > self.length:
			return
		curr = self.head
		for _ in range(index):
			curr = curr.next
		temp = curr.next
		curr.next = Node(val)
		curr.next.next = temp
		self.length += 1

	def deleteAtIndex(self, index: int) -> None:
		if index < 0 or index >= self.length:
			return
		curr = self.head
		for _ in range(index):
			curr = curr.next
		temp = curr.next
		curr.next = temp.next
		self.length -= 1
