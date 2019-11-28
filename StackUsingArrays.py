#########################################
## Name: Creating Stack using an Array ##
## Owner: Darshit Pandya               ##
## Purpose: Data structure practice    ##
#########################################

from sys import maxsize
class Stack():

	'''This class creates a stack using an array data structure.
	Some of the built-in methods of the arrays are taken into 
	consideration for the same '''

	def __init__(self):
		# creates an empty stack in form of an array
		self.stack = list() # we cannot use array.array() as it is datatype restricted

	def push(self, item_):
		# pushes the item in the stack
		self.stack.append(item_)

	def isEmpty(self):
		# check if the stack is empty
		if len(self.stack) == 0:
			return True
		else:
			return False

	def pop(self):
		# pops the top of the stack
		if self.isEmpty():
			print str(-maxsize - 1)
		
		print self.stack.pop()

	def peek_at_item(self):
		# look at the top of the stack without popping
		if self.isEmpty():
			return str(-maxsize - 1)

		return self.stack[-1]

if __name__ == "__main__":
	## Create an object of Stack Class

	stack_obj = Stack()

	for i in range(5):
		stack_obj.push(i)

	while not stack_obj.isEmpty():
		stack_obj.pop()


