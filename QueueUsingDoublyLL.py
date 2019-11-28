############################################
## Name: Queue using doubly linked list   ##
## Owner: Darshit Pandya                  ##
## Purpose: Data Structure Practice       ##
############################################

'''
Logic:
For every element insert, update the prev and the rear node.
The rear node will be the end node of insertion, always
'''
class Node():

	def __init__(self, data_):
		self.data = data_
		self.next = None
		self.prev = None

class Queue(Node):

	def __init__(self):
		self.front = None
		self.rear = None

	def is_empty(self):
		if self.front == None and self.rear == None:
			return True
		else:
			return False

	def is_full(self):
		## in linked list there is no way to know if the 
		## queue is full or not, hence will pass it as of now
		pass

	def enqueue(self, element_):
		temp = self.rear
		if temp == None:
			self.front = Node(element_)
			self.rear = self.front
		else:
			temp = Node(element_)
			self.rear.next = temp
			self.rear = self.rear.next

	def dequeue(self, print_ = 0):
		if self.is_empty():
			print("Queue is already empty")
			exit(1)

		temp = self.front
		self.front = self.front.next
		if print_ == 0:
			print("Dequeued: ", temp.data)

	def get_front(self):
		return self.front.data


	def get_rear(self):
		return self.rear.data

if __name__ == '__main__':
	queue_object = Queue()
	queue_object.enqueue(10)
	queue_object.enqueue(11)
	queue_object.enqueue(12)
	queue_object.enqueue(13)
	queue_object.enqueue(14)

	queue_object.dequeue()

	queue_object.get_front()
	queue_object.get_rear()