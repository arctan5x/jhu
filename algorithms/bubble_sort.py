def bubble_sort(lst):
	if not lst:
		return []
	for i in range(len(lst)):
		for j in range(1, len(lst)):
			if lst[j - 1] > lst[j]:
				lst[j - 1], lst[j] = lst[j], lst[j - 1]
	return lst

if __name__ == "__main__":
	# some tests
	lst1 = [2, 1, 34, 3, 6, 2, 4, 7]
	print bubble_sort(lst1) == [1, 2, 2, 3, 4, 6, 7, 34]
	lst2 = []
	print bubble_sort(lst2) == []
	lst3 = [1]
	print bubble_sort(lst3) == [1]
	lst4 = [2, 1]
	print bubble_sort(lst4) == [1, 2]
	lst5 = [1, 2, 3]
	print bubble_sort(lst5) == [1, 2, 3]