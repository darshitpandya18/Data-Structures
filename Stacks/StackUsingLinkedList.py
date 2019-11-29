############################################
## Name: Creating Stack using Linked List ##
## Owner: Darshit Pandya                  ##
## Purpose: Data structure practice       ##
############################################

class StackNode():
	'''This is the inner child class of each Node in 
	the stack'''

	def __init__(self, data_):
		self.data = data_
		self.next = None

class Stack(StackNode):
	'''This class creates a stack using a linked list
	dta structure'''

	def __init__(self):
		self.root =None 

	
	def isEmpty(self):
		if self.root == None:
			return True
		else:
			return False

	def push(self, data_):
		# pushes each of the 
		new_node = StackNode(data_)
		new_node.next = self.root
		self.root = new_node

	def pop(self):
		# returns the current root node as the head. Pop removes it from
		# the stack and hence to remove it from the linked list too
		if self.isEmpty():
			return float("-inf")
		else:
			temp = self.root
			self.root = self.root.next
			#print(temp.data)

	def peek(self):

		if self.isEmpty():
			return float("-inf")
		else:
			return self.root.data



if __name__ == "__main__":

	stack_object = Stack()

	print(stack_object.peek())
	print(stack_object.pop())
	stack_object.push(10)
	stack_object.push(20)
	stack_object.push(30)

	print(stack_object.peek())

