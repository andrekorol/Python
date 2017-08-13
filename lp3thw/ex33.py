numbers = []


def numbers_loop(top, increment):
    # i = 0
    for i in range(0, top, increment):
        # /rwhile i < top:
        print(f"At the top i is {i}")
        numbers.append(i)
        # i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")
    for num in numbers:
        print(num)


numbers_loop(10, 2)
