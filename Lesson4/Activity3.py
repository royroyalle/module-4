import array as arr
array_num = arr.array('i', [1, 2, 3, 3, 3, 3, 4, 5,])
print("Org Array:", array_num)
print("Number of occurances of 3 in the array:", array_num.count(3))
array_num.reverse()
print("Reverse of the array:")
print(array_num)
