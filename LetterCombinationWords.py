## Leetcode: 91

## generate the number of patterns possible for the given
## number array

class Solution:

	def __init__(self, nums_):
		self.nums = nums_
		self.solutions = list()

	def generate_solutions(self):
		
		for iterator in range(len(self.nums)):
			temp_1 = self.nums[:iterator]
			if iterator + 1 < len(self.nums):
				temp = str(self.nums[iterator]) + str(self.nums[iterator + 1])
				if int(temp) <= 26:
					temp_1.append(int(temp))
					temp_1.extend(self.nums[iterator+2:])
				else:
					temp_1.append(self.nums[iterator])
					temp_1.extend(self.nums[iterator+1:])
			else:
				temp_1.append(self.nums[iterator])
				temp_1.extend(self.nums[iterator+1:])

			
			if temp_1 not in self.solutions:
				self.solutions.append(temp_1)

		print(self.solutions)



solution = Solution([1,2,2,1])
solution.generate_solutions()