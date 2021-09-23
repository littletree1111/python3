class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, new_node):
		# check if head is empty
		if self.head:
			# get the last node
			last_node = self.head
			while last_node.next != None:
				last_node = last_node.next

			# assign new node to next pointer of last node
			last_node.next = new_node

		else:
			# head is empty
			# assign node to head
			self.head = new_node

	def display(self):
		# iterator
		temp_node = self.head

		# iterate until the end of linked list
		while temp_node != None:
			# print node data
			print(temp_node.data, end='->')

			# move iterator to the next node
			temp_node = temp_node.next

		print('Null')

if __name__ == '__main__':
	# instantiate linked list
	linked_list = LinkedList()

	# insert data into linked list
	linked_list.insert(Node(1))
	linked_list.insert(Node(2))
	linked_list.insert(Node(3))
	linked_list.insert(Node(4))
	linked_list.insert(Node(5))
	linked_list.insert(Node(6))
	linked_list.insert(Node(7))

	# print linked list
	linked_list.display()
