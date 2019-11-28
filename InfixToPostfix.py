###############################################################
## Name: Infix expression to Postfix expression using Stacks ##
## Owner: Darshit Pandya                                     ##
## Purpose: Data Structure Practice                          ##
###############################################################
from __future__ import print_function
import time
import six
class Node():
	"""
	This is a class to create item of the Stack in form a node of a linked list

	Attributes:
		data: (string or int) Value of each node
		next: pointer to next node(stack item here)
	"""

	def __init__(self, data_):
		self.data = data_
		self.next = None

class Stack(Node):

	"""
	This is a class for creating Stack using the concepts of the Linked List

	Attributes:
		root: initialized to None
	"""
	def __init__(self):
		self.root = None

	def is_empty(self):
		return self.root == None

	def push_(self, element_):
		# Stack can grow endlessly. No limit on the size of the stack
		node_ = Node(element_)
		node_.next = self.root
		self.root = node_

	def pop_(self):
		if self.is_empty():
			print("Stack Already Empty")
			exit(1)
		
		temp = self.root
		self.root = self.root.next
		print("Popped: ", temp)

	def pop_all(self):
		
		while not self.root == None:
			temp = self.root
			self.root= self.root.next
			print(temp)

	def peek_at_stack(self):
		
		top_of_stack = self.root
		print("Top of the stack is: ", top_of_stack)


if __name__ == '__main__':
	'''This code is about first taking the input from the user in form
	of a infix operation and then converting it into postfix operation

	How the algorithm works
	1. Output if the input is operand
	2. If the input is operator:
		a> If stack is empty or contains ')', push the operator
		b> If precedence(top of stack) < precedence(current item):
			i> Push the current item to the stack
			ii> Update the root of the stack i.e. the top of the stack
		c> If precedence(top of stack) >= precedence(current item):
			i> Pop all the operators whose precedence >= the scanned operator

		d> If scanned operator =='(', push it on the stack
		e> If scanned operator ==')', pop till '(' is received and discard both

	3. Repeat till the expression is completed
	'''
	stack_object = Stack()
	sequence_ = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 4, ')': 5}
	expression_ = six.moves.input("Enter the input infix expression: ")
	print(expression_)
	expression_ = expression_.lower()
	for char_ in expression_:
		ascii_= ord(char_)
		if ascii_ >= 97 and ascii_ <= 122:
			print(char_, end = "")

		elif ascii_ == 40:
			stack_object.push_(char_)

		elif ascii_ in [42, 43, 45, 47]:
			if stack_object.is_empty():
				pass
			else:   
                print(stack_object.root)
				if sequence_[stack_object.root] < sequence_[char_]:
					stack_object.push_(char_)
                elif sequence_[stack_object.root] >= sequence_[char_]:
                    while not stack_object.is_empty() and sequence_[stack_object.root] >= sequence_[char_]:
                        stack_object.pop_()
		elif ascii_ == 41:
			while not stack_object.root == '(':
				stack_object.pop()

			stack_object.pop()

	if not stack_object.is_empty():
		stack_object.pop_all()

	print("Infix expression: ", expression_)

	print("Corresponding Postfix expression: ")

###########################################################################################
##Note: To do infix to prefix: Reverse input string, convert all')' to '(' and vice versa;
##      perform postfix and then reverse the postfix
###########################################################################################