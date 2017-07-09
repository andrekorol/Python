numbers = []
x = 0
def add_numbers_to_list(starting_number, number_cap, incrementation, chosen_list):
	while starting_number < number_cap:
		chosen_list.append(starting_number)
		starting_number += incrementation
		print "Numbers now:", numbers

add_numbers_to_list(x, 99, 10, numbers)