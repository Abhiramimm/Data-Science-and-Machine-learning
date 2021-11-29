a = []
a1 = [2, 4, 6]
a.append(a1)
a2 = [4, 5, 6]
a.append(a2)
print(a)
b = []
b1 = [8, 10, 12]
b.append(b1)
b2 = [2, 4, 2]
b.append(b2)
print(b)
result = [[0, 0, 0],
         [0, 0, 0]]
print("Resultant matrix : ")
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]
for r in result:
    print(r)