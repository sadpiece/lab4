N = int(input("введіть N(кількість елементів масиву):"))

a = int(input("введідь елементи масиву"))

arr = [int(input()) for _ in range(N)]

arr.sort()
print("мінімальний елемент: ", arr[0])