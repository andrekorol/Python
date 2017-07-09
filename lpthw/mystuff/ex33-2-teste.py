numbers = []
x = 0

def add_numbers_to_list(starting_number, number_cap, incrementation, chosen_list):
	for i in range(starting_number, number_cap):
		chosen_list.append(i)
		starting_number += incrementation
		print numbers

add_numbers_to_list(0, 6, 1, numbers)