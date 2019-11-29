################################################
## Name: Implementation of Double Ended Queue ##
## Owner: Darshit Pandya                      ##
## Purpose: Data Structure Practice           ##
################################################

class DEQueue():

	def __init__(self, capacity):
		self.capacity = capacity
		self.dequeue = [None] * self.capacity
		self.front = -1
		self.rear = 0
		self.size = 0
		
	def is_empty(self):
		return self.front == -1

	def is_full(self):
		return self.rear == self.front - 1

	def insert_front(self, element_):
		"""
		Inserts the current element at the front end

		Arguments:
			- element_: The data to be entered
		"""
		if self.is_full():
			print("Double-ended queue already full")
			exit(1)

		if self.front == -1:
			self.front = 0
		elif self.front == 0:
			self.front = self.capacity - 1
		else:
			self.front = self.front - 1

		self.dequeue[self.front] = element_

	def insert_rear(self, element_):
		if self.is_full():
			print("Double-ended queue already full")
			exit(1)

		self.rear = self.rear + 1
		self.dequeue[self.rear] = element_

	def delete_front(self):
		if self.is_empty():
			print("Double-ended queue already empty")
			exit(1)

		if self.front == 0:
			self.front = -1
		else:
			self.dequeue[self.front] = None
			self.front = self.front + 1

	def delete_rear(self):
		if self.is_empty():
			print("Double-ended queue already empty")
			exit(1)
		if self.rear == 0:
			# means only one element exists which is front
			self.delete_front()
		else:
			self.dequeue[self.rear] = None
			self.rear = self.rear - 1

	def get_front(self):
		if self.is_empty():
			print("No front exists. Double-ended queue is empty")
			exit(1)
		return self.dequeue[self.front]

	def get_rear(self):
		if self.is_empty():
			print("No rear exists. Double-ended queue is empty")
			exit(1)
		return self.dequeue[self.rear]

if __name__ == '__main__':
	
	dequeue_object = DEQueue(5)
	dequeue_object.insert_front(10)
	#dequeue_object.insert_front(11)
	#dequeue_object.insert_front(12)

	#dequeue_object.insert_rear(13)
	#dequeue_object.insert_rear(14)

	print(dequeue_object.get_front())
	print(dequeue_object.get_rear())

	#dequeue_object.insert_front(15)
	dequeue_object.delete_rear()
	dequeue_object.get_front()