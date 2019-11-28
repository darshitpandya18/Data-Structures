## backtracking solution to find the solution to the sum of subsets problem
## we are not concerned about the complexity here as we are just trying to solve 
## the problem using the backtracking approach

import copy

class Solution:

	def __init__(self, input_array, k):
		self.array = input_array
		self.k = k
		self.solutions = list()
		self.target = 0
		self.visited = list()

	def backtrack(self, start = 0,  temp_array = []):

		if sum(temp_array) == self.target:
			sorted_temp_array = sorted(temp_array)
			if not sorted_temp_array in self.solutions:
				self.solutions.append(sorted_temp_array)
			return

		elif sum(temp_array) > self.target:
			return
		temp_ = temp_array
		for iterator_ in range(start, len(self.array)):
			temp_.append(self.array[iterator_])
			self.backtrack(iterator_ + 1, temp_)
			temp_.pop()
		return


	def find_all_solutions(self):
		## base case: sum(array) should be divisible by k
		if sum(self.array) % self.k == 0:
			self.target = sum(self.array) / self.k
			_ = self.backtrack()
			print(self.solutions)
		else:
			print("Can't divide given array in equal sum")
			exit(0)


## as an input, we need an array of nums and the number of partitions expected 
## to get the subarrays of equal sum
solution = Solution([4, 3, 2, 3, 5, 2, 1], 4)
solution.find_all_solutions()