#############################################
## Name: Tower of Hanoi(Iterative - Stack) ##
## Owner: Darshit Pandya                   ##
## Purpose: Data Structures Practice       ##
#############################################


from StackUsingLinkedList import Stack

moves_=  {1: "Source to Destination", 2: "Source to Auxiliary", 0: "Auxiliary to Destination"}

def swapping_function(stack_1, stack_2, move_):

	if stack_1.isEmpty():
		## stack 1 is empty then , stack1.root = stack2.root and pop from stack2
		print(stack_2.root.data, moves_[move_])
		stack_1.push(stack_2.root.data)
		stack_2.pop()
		

	elif stack_2.isEmpty():
		## stack 2 is empty then, stack2.root = stack1.root and pop from stack1
		print(stack_1.root.data, moves_[move_])
		stack_2.push(stack_1.root.data)
		stack_1.pop()
		

	else:
		## if none of them are empty, we will compare the elements from both of the stacks
		## the stack which has higher numbered top of the stack, we will move the disk
		## from the other stack to that stack
		top_1 = stack_1.root.data
		top_2 = stack_2.root.data
		if top_1 < top_2:
			print(stack_1.root.data, moves_[move_])
			stack_2.push(stack_1.root.data)
			stack_1.pop()
		elif top_1 > top_2:
			print(stack_2.root.data, moves_[move_])
			stack_1.push(stack_2.root.data)
			stack_2.pop()

def main(n, stack_source, stack_aux, stack_dest):

	"""
	Arguments:
		- n : number of disks
		- stack_source: Source Stack Object
		- stack_aux: Auxiliary Stack Object
		- stack_dest: Destination Stack Object 
	
	Intermediate Results:
		- Prints each move occuring in the process

	Returns:
		- d: The list of the final destination
	"""
	nmoves_ = 2**n - 1 # number of moves = 2^n - 1
	for i in range(n, 0, -1):
		stack_source.push(i)

	if n%2 == 0:
		## means the number of disks = even, hence, swap the aux with destination
		pass
	else:
		for i in range(1, nmoves_ + 1):
			if i % 3 == 0:
				swapping_function(stack_aux, stack_dest, 0)

			elif i % 3 == 1:
				swapping_function(stack_source, stack_dest, 1)

			elif i % 3 == 2:
				swapping_function(stack_source, stack_aux, 2)

	while not stack_dest.isEmpty():
		print(stack_dest.peek())
		stack_dest.pop()

if __name__ == '__main__':

	ndisks_ = 3
	stack_source = Stack()
	stack_aux = Stack()
	stack_destination = Stack()

	main(ndisks_, stack_source, stack_aux, stack_destination)