################################################
## Name: Implementation of Binary Tree        ##
## Owner: Darshit Pandya                      ##
## Purpose: Data Structure Practice           ##
################################################


## We find the empty node and insert the value in inorder.
## We use queue for inorder. Why?

class Node():

	def __init__(self, value_):
		self.left = None
		self.right = None
		self.val = value_

class BTree():
	
	def __init__(self):
		self.root = None

	def insert(self, value_):
		"""
		This function inserts the given Node value whose left or right is empty.
		Only one insertion is done. Break once done

		Arguments:
			value_: The value to be inserted in the given tree
		"""
		q = list()
		q.append(self.root)

		while len(q) > 0:

			temp = q[0]
			q.pop(0)

			if not temp.left:
				temp.left = Node(value_)
				break
			else:
				q.append(temp.left)

			if not temp.right:
				temp.right = Node(value_)
				break
			else:
				q.append(temp.right)

	def inorder_traversal(self, temp):
		"""
		This function performs the inorder traversal of the given binary tree
		left root right. 
		"""
		if (not temp):
			return
		else:
			self.inorder_traversal(temp.left)
			print(temp.val)
			self.inorder_traversal(temp.right)

	def postorder_traversal(self, temp):

		if not(temp):
			return
		else:
			self.postorder_traversal(temp.left)
			self.postorder_traversal(temp.right)
			print(temp.val)

	def find_node(self, value_):
		"""
		Find the node in the tree.
		"""
		q = list()
		q.append(self.root)
		node_found = None
		deepest_node = None
		deepest_node_parent = None
		position_ = None

		while len(q):
			temp = q[0]
			q.pop(0)

			if temp.val == value_:
				node_found = temp
			if temp.left:
				q.append(temp.left)
				deepest_node = temp.left
				deepest_node_parent = temp
				position_ = "left"
			if temp.right:
				q.append(temp.right)
				deepest_node = temp.right
				deepest_node_parent = temp
				position_ = "right"

		## we pop from q but not q_, so the last element in the q_ will be the deepest node
		return node_found, deepest_node, deepest_node_parent, position_

	def delete_node(self, value_):
		"""
		This function deletes the node from the given binary tree.
		It replaces the node to be deleted with the deepest node in the tree

		Process:
			1. Check if the root is empty. Or else the tree is empty
			2. Search the tree and find the deepest node. We will optimize the approach here.
		"""
		
		if not self.root:
			return None
		if not self.root.left and not self.root.right:
			if self.root.val == value_:
				return self.root
			else:
				return None


		node_, deepest_node, deepest_node_parent, position_ = self.find_node(value_)
		if node_:
			temp_val = deepest_node.val
			node_.val = temp_val
			if position_ == "right":
				deepest_node_parent.right = None
			else:
				deepest_node_parent.left = None

			return "0"

		else:
			return None




if __name__ == '__main__':
	btree = BTree()
	btree.root = Node(10)
	l11 = Node(11)
	r11 = Node(9)

	l21 = Node(7)
	l22 = Node(15)

	r22 = Node(8)

	btree.root.left = l11
	btree.root.right = r11

	l11.left = l21
	r11.left = l22
	r11.right = r22

	## before insertion
	#btree.inorder_traversal(btree.root)

	## insertion
	btree.insert(12)

	## after insertion
	btree.inorder_traversal(btree.root)
	#btree.postorder_traversal(btree.root)

	## deletion of a node from a tree
	ret = btree.delete_node(11)
	print("------------------------------------")

	## print tree after deletion
	btree.inorder_traversal(btree.root)