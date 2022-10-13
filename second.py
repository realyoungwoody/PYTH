a = int(input("Введите размер массива "))
x = [0] * a
for i in range(a):
    x[i] = float(input())
print(x)
b = int(input("Введите размер массива "))
y = [0] * b
for i in range(b):
    y[i] = float(input())
print(y)
c = list(set(x) & set(y))
print(c)
input()



