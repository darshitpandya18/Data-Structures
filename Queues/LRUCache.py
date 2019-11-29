############################################
## Name: Implementing LRU cache using LL  ##
## Owner: Darshit Pandya                  ##
## Purpose: Data Structure Practice       ##
############################################

'''
Logic:

- The front node always refers to the one that is least used
- If we use stack, the least used will always be on top and hence we use queue data structure
- We maintain the hash value of the elements in the queue to check if the page is present
- If the page is present, we will consider it a hit
- If the page is not present:
	- Consider it as a page fault and increment it's value
	- remove the page from the front
	- add the current page to the rear part of the queue
- Return the number of the hits and page faults

@Inputs:
	: frame_size: number of frames for paging
	: page_access: input list of page access sequence
'''

from QueueUsingDoublyLL import Queue

def main(frame_size, page_access):
	 if frame_size == 0:
	 	print("Frame size value should be greater than 1")
	 	exit()

	 elif page_access == "":
	 	print("No Page Access sequence passed.")
	 	exit()

	 queue_object = Queue()
	 hash_dict = dict()
	 hits_ = 0
	 faults_ = 0
	 hits_seq = list()
	 faults_seq = list()

	 sequences_ = map(int, page_access.strip().split(", "))
	 for page_ in sequences_:
	 	if len(hash_dict.keys()) == frame_size:
	 		# means all the frames are having pages inside them
	 		# need to remove the least used
	 		if page_ in hash_dict.keys():
	 			hits_ += 1
	 			hits_seq.append(page_)
	 			queue_object.dequeue(1)
	 			queue_object.enqueue(page_)
	 			
	 		else:
	 			faults_ += 1
	 			faults_seq.append(page_)
	 			lru_ = queue_object.get_front()
	 			queue_object.dequeue(1)
	 			queue_object.enqueue(page_)
	 			del hash_dict[lru_]
	 			hash_dict[page_] = queue_object.rear
	 			
	 	else:
		 	queue_object.enqueue(page_)
		 	hash_dict[page_] = queue_object.rear
	 		faults_+=1

	 return hits_, hits_seq, faults_, faults_seq
	 	

if __name__ == '__main__':

	frame_size = 3
	page_access= "1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5"
	hits_, hits_seq, faults_, page_faults_seq = main(frame_size, page_access)
	print("Hits of Pages: ", str(hits_seq))
	print("Number of Hits: ", hits_)
	print("Faults Sequence: ", str(page_faults_seq))
	print("Number of Faults", faults_)