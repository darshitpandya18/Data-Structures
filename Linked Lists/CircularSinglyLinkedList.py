#########################################
## Name: Circular Singly Linked List   ##
## Owner: Darshit Pandya               ##
## Purpose: Practice                   ##
#########################################

class Node():
	'''creates each node in the linked list'''

	def __init__(self, data = ""):
		self.data = data
		self.next = None


class CircularSinglyLinkedList(Node):
	'''class that creates the circular singly linked list'''

	def __init__(self):
		self.head = None

	def link_the_list(self, data_):
		# this code recursively links the data in the linked list
		return Node(data_)


	def print_linkedlist(self):
		'''This function prints the given linked list in a formatted
		format'''
		temp = self.head
		print(temp.data)

		while not temp.next == self.head:
			temp = temp.next
			print(temp.data)


if __name__ == "__main__":

	## Create a dummy list of elements to create a circular linked list
	list_temp = [10, 11, 12, 13, 14]

	cll = CircularSinglyLinkedList()
	cll.head = Node(10)
	node_1 = Node(11)
	node_2 = Node(12)
	node_3 = Node(13)
	node_4 = Node(14)

	cll.head.next = node_1
	node_1.next = node_2
	node_2.next = node_3
	node_3.next = node_4
	node_4.next = cll.head

	cll.print_linkedlist()


