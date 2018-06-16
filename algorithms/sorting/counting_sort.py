import sys

def counting_sort(arr):
	if len(arr) < 2:
		return arr

	max_val = sys.maxint * -1
	for element in arr:
		if element > max_val:
			max_val = element

	count_store = [0] * max_val

	for element in arr:
		count_store[element - 1] += 1

	for i in range(1, len(count_store)):
		count_store[i] = count_store[i-1] + count_store[i]

	return_lst = [0] * len(arr)
	for element in arr:
		index = count_store[element - 1]
		count_store[element - 1] -= 1
		return_lst[index - 1] = element

	return return_lst



if __name__ == "__main__":
	# some tests
	lst1 = [2, 1, 34, 3, 6, 2, 4, 7]
	print(counting_sort(lst1) == [1, 2, 2, 3, 4, 6, 7, 34])
	lst2 = []
	print(counting_sort(lst2) == [])
	lst3 = [1]
	print(counting_sort(lst3) == [1])
	lst4 = [2, 1]
	print(counting_sort(lst4) == [1, 2])
	lst5 = [1, 2, 3]
	print(counting_sort(lst5) == [1, 2, 3])
	lst6 = [2, 1, 34, 3, 6, 2, 4, 7, 5, 6, 6, 89, 2]
	print(counting_sort(lst6) == [1, 2, 2,2, 3, 4, 5, 6, 6, 6, 7, 34, 89])