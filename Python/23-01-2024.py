#Find the sum of the second largest number in a sub-list => Input = [[1, 2, 3], [2, 4, 1, 0]] Output = 2+2 = 4

nested_list = [[1, 2, 3], [2, 4, 1, 0]]

# Printing all the elements of a nested list
for sublist in nested_list:
    sublist.sort()
a=nested_list[0][-2] + nested_list[1][-2]
print(a)







