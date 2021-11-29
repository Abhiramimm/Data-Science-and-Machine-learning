lst1 = []
n1 = int(input("Enter number of elements : "))
print("Enter elements in to list 1:")
for i in range(0, n1):
    ele = int(input())
    lst1.append(ele)
print("List 1: ",lst1)
lst2 = []
n2 = int(input("Enter number of elements : "))
print("Enter elements in to list 1:")
for i in range(0, n2):
    ele = int(input())
    lst2.append(ele)
print("List 2: ",lst2)
res_lt = []
for x in range(0, len(lst1)):
    res_lt.append(lst1[x] + lst2[x])
print("Addition of the list 1 and 2 is: " + str(res_lt))