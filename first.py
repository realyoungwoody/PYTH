y = int(input("Введите размер массива "))
x = [0] * y
for i in range(y):
    x[i] = float(input())
print(x)
print(max(x))
input()
