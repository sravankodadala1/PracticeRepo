# swap first and last elements in a list
Input = [12, 35, 9, 56, 24]
a = len(Input) - 1
print(a)
for i in range(len(Input)):
    Input[i], Input[a] = Input[a], Input[i]
    break
print(Input)



# swap positions in a list
List = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

List[pos1], List[pos2] = List[pos2], List[pos1]
print(List)



# insert a string alternatively in a list
list = ["apple", "orange", "grape"]

a = 0
for i in range(len(list)):
    list.insert(a, "c")
    a = a + 2
print(list)



# iterate two lists simultaneously
a = [1, 2, 3]
b = ["a", "b", "c"]
l = []
for (i, j) in zip(a, b):
    l.append([i, j])
print(l)



#avg of each list in nestd list [2.3333333333333335, 7.333333333333333, 15.333333333333334]
a=[[1,2,4],
   [4,5,6],
   [7,8,9]]

list=[]
for i in a:
    sum=0
    b=len(i)
    for j in i:
        sum=sum+j
    list.append(sum/b)
print(f"avg of each list in nestd list {list}")


#count occurence in a list
a=[1,2,3,4,5,5,5,5,5,5]
count=0
for i in a:
    if i==5:
        count=count+1
print(count)


#index of a first occurence of element in list
a=[1,2,3,4,5,5]

element=5

for i in range(len(a)):
    if a[i]==element:
        print(i)
        break



#flatten a list
a=[[1,2],[3,4],[5,6]]
b=[]
for i in a:
    for j in range(len(i)):
        b.append(i[j])

print(b)


#largest element in a nested list
a=[[1,10,2,3],[4,2,7]]

max=0
for i in a:
    for j in i:
        if j>max:
            max=j
print(f"max value in nested list is {max}")


#sort a list
a=[2,3,1,5,4]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)


#inserting a string alternatively in a list
list=["apple","orange","grape"]

a=0
for i in range(len(list)):

    list.insert(a,"c")
    a=a+2
print(list)