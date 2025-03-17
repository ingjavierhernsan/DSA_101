my_array = [7, 3, 9, 12, 11]

print("Array: ", my_array)

n = len(my_array)
for i in range(n-1):
	swapped = False
	for j in range(n-i-1):
		if my_array[j] > my_array[j+1]:	
			#Solution 1
			temp_num = my_array[j]
			my_array[j] = my_array[j+1]
			my_array[j+1] = temp_num
			
			#Solution 2
			#my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

			swapped = True
		if not swapped:
			break

print("Sorted array: ", my_array)