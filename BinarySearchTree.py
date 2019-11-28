################################################
## Name: Implementation of Binary Search Tree ##
## Owner: Darshit Pandya                      ##
## Purpose: Data Structure Practice           ##
################################################

class Node:

	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

class BSTree(Node):

	def __init__(self):
		self.root = None

	def creation_(self, list_values):
		"""
		Create a Binary Search Tree using the given values

		Arguments:
			list_values: List of values to create the binary search tree
		"""
		
