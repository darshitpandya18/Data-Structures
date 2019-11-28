###############################################
## Name: Creating K stacks in a single array ##
## Owner: Darshit Pandya                     ##
## Purpose: Data Structures Practice         ##
###############################################

class KStacks():

	'''This class is all about creating k stacks in a single array '''
	def __init__(self, stacks_count, size_):

		self.k = stacks_count
		self.n = size_

		self.top_tracker = [-1] * self.k
		self.array_ = [None] * self.n

		self.free = 0
		self.next = [i + 1 for i in range(self.n)] ## we need this as we are not dividing the whole array in fixed set sizes
		self.next[self.n - 1] = -1


	def is_empty(self,stack_number):
		## Checks if the given stack number stack is empty or not
		if self.top_tracker[stack_number] == -1:
			return True
		else:
			return False		

	def is_full(self):
		## Checks if the given stack number is full or not
		if self.free == -1:
			return True
		else:
			return False

	def print_stack(self, stack_number):
		## Given the stack number, it checks the top of the stack and
		## accesses the next list to find the linked elements of that 
		## stack

		if not self.is_empty(stack_number):
			
			temp = self.top_tracker[stack_number]
			while temp !=-1:
				print(self.array_[temp])
				temp = self.next[temp]
		else:
			print("Stack is Empty. Can't print anything")
			exit(1)

	def push_(self, stack_number, element):
		## This function pushes the element in the given stack
		## and updates the top of the stack in that element
		if not self.is_full():
		# Step 1: Check which variable is free
			insert_at = self.free

			# Step 2: Insert the element at the free space
			self.array_[insert_at] = element
			self.free = self.next[self.free]
			# Step 3: For the particular stack, change the pointer
			self.next[insert_at] = self.top_tracker[stack_number]

			# Step 4: Set the next free variable and the top of the stack for the particular stack
			self.top_tracker[stack_number] = insert_at
				
		else:
			print("Stack Overflow")
			exit(1)

	def pop_(self, stack_number):
		## Pops the top of the given stack_number stack
		
		if not self.is_empty(stack_number):

			## Step 1: Access the top of the stack of the given stack
			top_of_stack = self.top_tracker[stack_number]

			## Step 2: Remove the element from the stack(array)
			value_tos = self.array_[top_of_stack]

			## Step 3: Change the top of the stack to the next(current)
			self.top_tracker[stack_number] = self.next[top_of_stack]

			## Step 4: Change the next(current) with -1
			self.next[top_of_stack] = self.free 
			self.free = top_of_stack
			return value_tos

		else:

			print("Stack is empty")
			exit(1)

if __name__ =='__main__':

	## Create an object of the class
	stack_obj = KStacks(3, 10)
	stack_obj.push_(0, 10)
	stack_obj.push_(0, 11)
	stack_obj.push_(0, 17)
	stack_obj.push_(0, 18)

	stack_obj.push_(1, 12)
	stack_obj.push_(1, 13)
	stack_obj.push_(1, 19)
	stack_obj.push_(1, 20)

	stack_obj.push_(2, 14)
	stack_obj.push_(2, 15)
	#stack_obj.print_stack(1)
	stack_obj.pop_(2)
	stack_obj.pop_(2)
	stack_obj.push_(2, 21)
	#print(stack_obj.pop_(2))




