def merge_sort(lst):
	if not lst:
		return []
	elif len(lst) == 1:
		return lst

	# Split lists into two
	left = lst[:len(lst)//2]
	right = lst[len(lst)//2:]

	# Recursive merge_sort calls
	sorted_left = merge_sort(left)
	sorted_right = merge_sort(right)

	# Merge two sorted lists
	merged_lst = []
	left_index = 0
	right_index = 0
	while left_index < len(sorted_left) and right_index < len(sorted_right):
		if sorted_left[left_index] > sorted_right[right_index]:
			merged_lst.append(sorted_right[right_index])
			right_index += 1
		else:
			merged_lst.append(sorted_left[left_index])
			left_index += 1

	if left_index != len(sorted_left):
		merged_lst.extend(sorted_left[left_index:])
	else:
		merged_lst.extend(sorted_right[right_index:])
	return merged_lst

if __name__ == "__main__":
	# some tests
	lst1 = [2, 1, 34, 3, 6, 2, 4, 7]
	print merge_sort(lst1) == [1, 2, 2, 3, 4, 6, 7, 34]
	lst2 = []
	print merge_sort(lst2) == []
	lst3 = [1]
	print merge_sort(lst3) == [1]
	lst4 = [2, 1]
	print merge_sort(lst4) == [1, 2]
	lst5 = [1, 2, 3]
	print merge_sort(lst5) == [1, 2, 3]