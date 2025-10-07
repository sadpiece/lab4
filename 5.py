def func():
    A = input("введіть текст: ")

    repeat = []
    single = []

    for char in A.lower():
        if char.isalpha():  # ← додаємо перевірку на літеру
            count = A.lower().count(char)
            if count >= 2 and char not in repeat:
                repeat.append(char)
            elif count == 1 and char not in single:
                single.append(char)

    print("Літери, які входять не менше двох разів:", repeat)
    print("Літери, які входять по одному разу:", single)


func()