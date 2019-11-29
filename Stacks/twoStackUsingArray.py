##############################################
## Name: Creating two stacks using an array ##
## Owner: Darshit Pandya                    ##
## Purpose: Data Structures Practice        ##
##############################################

class TwoStacks():

	def __init__(self, n):
		self.n = n
		self.top1 = -1
		self.top2 = self.n
		self.array_ = [None] * self.n


	def push_1(self, element):

		if self.top1 < self.top2 - 1:
			self.top1 = self.top1 + 1
			self.array_[self.top1] = element
		else:
			print("Stack Overflow")
			exit(1)

	def push_2(self, element):

		if self.top1 < self.top2 - 1:
			self.top2 = self.top2 - 1
			self.array_[self.top2] = element
		else:
			print("Stack Overflow")
			exit(1)

	def pop_1(self):
		## returns the top of the stack of the first stack

		if self.top1 > -1:
			popped_value = self.array_[self.top1]
			self.array_[self.top1] = None
			self.top1 = self.top1 - 1
			return popped_value
		else:
			print("Stack empty")
			exit(1)

	def pop_2(self):
		## returns the top of the stack for the second stack

		if self.top2 < self.n:
			popped_value = self.array_[self.top2]
			self.array_[self.top2] = None
			self.top2 = self.top2 + 1
			return popped_value

		else:
			print("Stack Empty")
			exit(1)

if __name__ == "__main__":

	twostacks = TwoStacks(5)
	twostacks.push_1(10)
	twostacks.push_1(11)

	twostacks.push_2(12)

	print("Pop from the first stack: ", twostacks.pop_1())
	print("Pop from the second stack: ", twostacks.pop_2())

	## Let's verify stack empty scenario
	twostacks.pop_2()



