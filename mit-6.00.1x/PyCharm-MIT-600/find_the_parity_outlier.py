def find_outlier(integers):
    odd = 0
    even = 0
    odd_list = []
    even_list = []
    for num in integers:
        if num % 2 != 0:
            odd += 1
            odd_list.append(num)
        else:
            even += 1
            even_list.append(num)
    if odd > even:
        for num in integers:
            if num not in odd_list:
                return num

    else:
        for num in integers:
            if num not in even_list:
                return num
