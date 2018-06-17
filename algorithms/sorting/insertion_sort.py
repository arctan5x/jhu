def insertion_sort(lst):
	if not lst:
		return []

	for i in range(1, len(lst)):
		pivot_key = lst[i]
		position = i - 1
		while position > -1 and pivot_key < lst[position]:
			lst[position + 1] = lst[position]
			position -= 1
		lst[position + 1] = pivot_key
	return lst


if __name__ == "__main__":
	# some tests
	lst1 = [2, 1, 34, 3, 6, 2, 4, 7]
	print insertion_sort(lst1) == [1, 2, 2, 3, 4, 6, 7, 34]
	lst2 = []
	print insertion_sort(lst2) == []
	lst3 = [1]
	print insertion_sort(lst3) == [1]
	lst4 = [2, 1]
	print insertion_sort(lst4) == [1, 2]
	lst5 = [1, 2, 3]
	print insertion_sort(lst5) == [1, 2, 3]