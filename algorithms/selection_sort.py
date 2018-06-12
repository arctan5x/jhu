def selection_sort(lst):
	if not lst:
		return []
	for i in range(len(lst)):
		smallest = i
		for j in range(i + 1, len(lst)):
			if lst[j] < lst[smallest]:
				smallest = j
		if smallest != i:
			lst[i], lst[smallest] = lst[smallest], lst[i]
	return lst

if __name__ == "__main__":
	# some tests
	lst1 = [2, 1, 34, 3, 6, 2, 4, 7]
	print selection_sort(lst1) == [1, 2, 2, 3, 4, 6, 7, 34]
	lst2 = []
	print selection_sort(lst2) == []
	lst3 = [1]
	print selection_sort(lst3) == [1]
	lst4 = [2, 1]
	print selection_sort(lst4) == [1, 2]
	lst5 = [1, 2, 3]
	print selection_sort(lst5) == [1, 2, 3]