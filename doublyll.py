class Node:
	def __init__(self, data):
		self.prev = None
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, new_node):
		# check if is head empty
		if self.head:
			# move to last node
			last_node = self.head
			while last_node.next != None:
				last_node = last_node.next

			new_node.prev = last_node
			last_node.next = new_node
		# if head is None, set new head
		if self.head == None:
			self.head = new_node


	def display(self):
		# print data in order
		print('Order: ', end='')

		temp_node = self.head
		while temp_node != None:
			print(temp_node.data, end='')
			temp_node = temp_node.next
		print()
		# print in reverse order
		print('Reverse order: ', end='')

		# move to last node
		last_node = self.head
		while last_node.next != None:
			last_node = last_node.next

		temp_node = last_node
		while temp_node != None:
			print(temp_node.data, end='')
			temp_node = temp_node.prev
		print()


if __name__ == '__main__':
	linked_list = LinkedList()

	linked_list.insert(Node(1))
	linked_list.insert(Node(2))
	linked_list.insert(Node(3))
	linked_list.insert(Node(4))
	linked_list.insert(Node(5))
	linked_list.insert(Node(6))
	linked_list.insert(Node(7))
	linked_list.insert(Node(8))
	
	linked_list.display()
