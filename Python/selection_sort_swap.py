my_array = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(my_array)

print("Array: ", my_array)

for i in range(n-1):
    min_index = i

    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
            
    #Solution 1
    temp_num = my_array[i]
    my_array[i] = my_array[min_index]
    my_array[min_index] = temp_num

    #Solution 2
    #my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("Sorted array: ", my_array)
