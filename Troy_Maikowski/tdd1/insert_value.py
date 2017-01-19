def insert_val_at(index, my_list, value):
	if not my_list:
		print "List is empty"
		return False
	elif index >= len(my_list):
		print "Out of Bounds"
		return False
	my_list.append(None)
	position = len(my_list) - 1
	while my_list[index] is not None:
		temp = my_list[position]
		my_list[position] = my_list[position - 1]
		my_list[position - 1] = temp
		position -= 1
	my_list[index] = value
	return my_list