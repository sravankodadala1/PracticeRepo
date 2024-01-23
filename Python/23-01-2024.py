def sum(input):
    result = 0

    for sublist in input:
        sublist.sort()
        if len(sublist) > 1:
            result += sublist[-2]

    return result

my_list = [[1, 2, 3], [2, 4, 1, 0]]
sum = sum(my_list)
print(sum)




