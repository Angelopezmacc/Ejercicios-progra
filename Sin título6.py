fibonacci=[0]
a=0
b=1
num = int(input("Numero de elementos:"))
for q in range(num):
    fibonacci.append(a+b)
    c = a + b
    a = b
    b = c
print(fibonacci)