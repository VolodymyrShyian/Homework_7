def common_elements():
		list_1 = [num_3 for num_3 in range(0, 100) if num_3 % 3 == 0]
		list_2 = [num_5 for num_5 in range(0, 100) if num_5 % 5 == 0]
		return set(list_1) & set(list_2)
		#num_3 for num_3 in range(0, 100) if num_3 % 3 == 0
		#num_5 for num_5 in range(0, 100) if num_5 % 5 == 0




assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
