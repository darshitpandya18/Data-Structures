###################################################
## Name: Queue Class implementation using Arrays ##
## Owner: Darshit Pandya                         ##
## Purpose: Data Structures Practice             ##
###################################################

class Queue():
	"""
	This class implements the basic queue operations
	viz. isFull(), isEmpty(), enQueue(), deQueue(),
	getFront(), getRear()

	In a queue, we have two pointers, one that is pointing
	towards the front while other that is pointing towards the
	rear part of the queue. It's a FIFO data structure
	"""

	def __init__(self, capacity):
		"""
		Arguments:
			- capacity: The capacity of the queue to avoid memory overflow
		"""
		self.queue = [None]*capacity
		self.capacity = capacity
		self.front = 0
		self.rear = self.capacity - 1
		self.size = 0
		

	def isFull(self):
		"""
		Checks if the queue is full. If length of the array = capacity
		"""
		return self.size == self.capacity


	def isEmpty(self):
		"""
		Checks if the queue is empty. Front and Rear are at the same position.
		"""
		if self.size == 0:
			return True
		else:
			return False

	def enQueue(self, data_):
		"""
		Adds an element to the end of queue.

		Arguments:
			- data_: The element you need to add to the queue
		"""
		if self.isFull():
			print("Can't insert the data in the queue: Queue Full")
			exit(1)

		## This enqueuing logic using the concept of circular
		## movement to avoid the overhead of the transfer

		self.rear = (self.rear + 1) % self.capacity
		self.queue[self.rear] = data_
		self.size = self.size + 1


	def deQueue(self):
		"""
		Removes an element from the top of the queue i.e. the element
		referred by front pointer of the queue
		"""
		if self.isEmpty():
			print("Queue already empty: Queue Empty")
			exit(1)
		print("Dequeueing: ", self.queue[self.front])
		self.queue[self.front] = None
		self.front = self.front + 1
		self.size = self.size - 1

	def getFront(self):
		"""
		Gets the element at the front of the queue
		"""
		front = self.queue[self.front]
		return front
		pass

	def getRear(self):
		"""
		Gets the element at the rear of the queue
		"""
		rear = self.queue[self.rear]
		return rear

if __name__ == '__main__':
	
	queue_object = Queue(10) # 10 = size of the queue
	queue_object.enQueue(11)
	queue_object.enQueue(12)
	queue_object.enQueue(13)
	queue_object.enQueue(14)

	while not queue_object.isEmpty():
		queue_object.deQueue()


