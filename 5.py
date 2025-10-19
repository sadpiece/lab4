def func():
    A = input("введіть текст: ")

    repeat = set()
    single = set()

    for char in A.lower():
        if char.isalpha():
            count = A.lower().count(char)
            if count >= 2:
                repeat.add(char)
            elif count == 1:
                single.add(char)

    print("Літери, які входять не менше двох разів:", repeat)
    print("Літери, які входять по одному разу:", single)


func()