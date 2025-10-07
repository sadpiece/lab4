def func():

    A = list(map(int, input('введіть список: ').split()))
    while len(A) < 4:
        print("Кількість елементів списку менше ніж 4")
        A = list(map(int, input('введіть список: ').split()))


    A.sort()


    print("Перші 5 максимальних елементів:", A[-5:] )
    return A

func()