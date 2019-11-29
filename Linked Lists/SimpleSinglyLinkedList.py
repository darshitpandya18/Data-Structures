##This class creates a linked list in python.
##We will create four node linked list in this program

class Node():

	def __init__(self, data):
		## create data node with a reference pointer to the next
		self.data = data
		self.next = None

class SimpleSinglyLinkedList(Node):
	## Each part of the linked list will be a Node
	## and hence it will inherit the Node class

	def __init__(self):
		self.head = None

	def print_linkedlist(self):
		## this general-purpose function will iterate over a linked list and will print it
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

	def add_node_at_front(self, new_node):
		## this function the original linkedlist object and the new node. It will then
		## add the new node as the first node to the given linkedlist

		new_node.next = self.head
		self.head = new_node

	def add_after_given_node(self, new_node, position_):
		## this function adds the new node at a given position.
		counter = 0
		self = self.head
		while not counter == position_:
			self = self.next
			counter += 1
		new_node.next = self.next
		self.next = new_node

	def add_at_end(self, new_node):
		## this function adds the new node at the end of the given linked list
		
		self = self.head
		while self.next:
			self = self.next

		self.next = new_node
		new_node.next = None

	def search_an_element(self, value_):
		## this function searches for the given node in the given linked list

		current = self.head
		counter = 1
		while current:
			## check till the data is not found
			if current.data == value_:
				return counter
			else:
				current = current.next
				counter += 1
		return -1

	def nth_from_end(self, position_):
		## this function finds a particular node at nth index from the end
		## for e.g if position_ = 3, I want the 3rd element from the end
		## i.e the 5th element in the array of 7(length - position_ + 1)
		## we will use the method of two pointers here.
		pointer_1 = self.head
		pointer_2 = self.head

		counter = 1
		while pointer_1:
			pointer_1 = pointer_1.next
			counter += 1
			if counter == position_:
				break

		while pointer_1.next:
			pointer_1 = pointer_1.next
			pointer_2 = pointer_2.next

		return pointer_2.data

if __name__ == "__main__":

	ll = SimpleSinglyLinkedList() # create an object
	ll.head = Node(10)
	node_1 = Node(11)
	node_2 = Node(12)
	node_3 = Node(13)

	## After the nodes are created, we need to link them together
	ll.head.next = node_1
	node_1.next = node_2
	node_2.next = node_3

	node_4 = Node(15) #start
	node_5 = Node(16) #positioned
	node_6 = Node(17) #end

	## Add this to the beginning
	ll.add_node_at_front(node_4)


	## Add a node after a particular position
	ll.add_after_given_node(node_5, 2)

	## Add a node at the end
	ll.add_at_end(node_6)
	ll.print_linkedlist()

	## search for the element in the given linked list
	position_ = ll.search_an_element(19)
	if position_ == -1:
		print("Element not found in the given linked list")
	else:
		print("Element found at position: ", position_)

	print("The nth element from end is: ", ll.nth_from_end(3))





