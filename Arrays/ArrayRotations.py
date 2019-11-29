class ArrayRotations():
	'''
	This class contains all the different ways to rotate 
	an array. For the time-being purpose, we will consider the 
	array to be a list
	'''

	
	def _gcd(self, a, b):

		if(b == 0):
			return a 

		else:
			return self._gcd(b, a%b)

	def method_1(self, original_array, rotation_count):
		'''Creates another array and then using slicing it rotates'''
		'''Time complexity O(n) and space complexity O(2N)'''
		temp = original_array[:rotation_count]
		original_array = original_array[rotation_count:] + temp
		return original_array

	def method_2(self, original_array, rotation_count):

		'''This method rotates by using a loop of the rotation_count'''
		for i in range(rotation_count):
				original_array = original_array[1:] + [original_array[0]]

		return original_array

	def method_3(self, original_array, rotation_count):
		'''This method is implemented using the juggling method'''
		'''refer geeksforgeeks.org python array problems for reference'''
		gcd = self._gcd(rotation_count, len(original_array))
		for i in range(gcd):
			
			# store the initial value of the set in a temporary variable
			temp = original_array[i]
			current_element = i

			while True:
				next_element = current_element + rotation_count

				if next_element >= len(original_array):
					next_element = next_element - len(original_array)

				if next_element == i:
					## it means it has reached the end of iteration for the current set
					break

				original_array[current_element] = original_array[next_element]
				current_element = next_element

			original_array[current_element] = temp

		print(original_array)


		


rotations_obj = ArrayRotations()
print(rotations_obj.method_1([1,2,3,4,5], 2))
print(rotations_obj.method_2([1,2,3,4,5], 2))
rotations_obj.method_3([1,2,3,4,5,6], 2)


