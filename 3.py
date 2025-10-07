def delete():

    A = list(map(int, input('введіть список: ').split()))
    while len(A) < 4:
        print("Кількість елементів списку менше ніж 4")
        A = list(map(int, input('введіть список: ').split()))

    print("введений список:", A)

    del A[1]
    del A[-2]


    print("Список після видалення другого і передостаннього елемента:", A)
    return A


delete()

