fibo=[0]
a=0
b=1
num = int(input("Numero de veces que se realice la sucesión de Fibonacci:"))
for q in range(num):
    fibo.append(a+b)
    c = a + b
    a = b
    b = c
print(fibo)