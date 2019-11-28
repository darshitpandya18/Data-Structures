########################################
## Built-in Data Structures in Python ##
## Creator: Darshit Pandya            ##
########################################

### 1st Way: Using an list

'''list_1 = []

list_1.append(0)
list_1.append(1)
list_1.append(2) ##<----- Last in 

print(list_1)
print(list_1.pop())''' ## <----- Last in will be the first out LIFO = Stack

### 2nd Way: using the collection.deque() : O(1) to access and insert: efficient way

'''from collections import deque

deque_1 = deque()
deque_1.append(0)
deque_1.append(1)
deque_1.append(2) ##<--------- This will be the last in

print(deque_1)
print(deque_1.pop())''' ##<------- Last in will be the first out LIFO = Stack

### 3rd Way: Using the LifoQueue which is used for concurrency too

from queue import LifoQueue
lifoqueue = LifoQueue()

lifoqueue.add(1)
lifoqueue.add(2)
lifoqueue.add(3) ## <---- Last in

print(lifoqueue)
print(lifoqueue.get()) ##<----- Last in will be first out


#import heapq
##heapq.heappush
##heapq.heappop

## from queue import PriorityQueue
## pq = PriorityQueue()
## pq.put()
## pq.get()