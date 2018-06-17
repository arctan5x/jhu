def get_heap_parent(index):
	return (index // 2) - 1

def get_heap_left(index):
	return (index * 2) + 1

def get_heap_right(index):
	return (index * 2) + 2

def heap_sort(arr):
	arr = build_max_heap(arr)
	length = len(arr)
	for i in range(len(arr) - 1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		length -= 1
		arr = max_heapify(arr, 0, length)
	return arr

def max_heapify(arr, index, length):
	left_index = get_heap_left(index)
	right_index = get_heap_right(index)
	largest = index
	if left_index < length and arr[index] < arr[left_index]:
		largest = left_index
	if right_index < length and arr[largest] < arr[right_index]:
		largest = right_index
	if largest != index:
		arr[index], arr[largest] = arr[largest], arr[index]
		max_heapify(arr, largest, length)
	return arr

def build_max_heap(arr):
	mid_bound = (len(arr)-1) // 2
	for index in range(mid_bound, -1, -1):
		max_heapify(arr, index, len(arr))
	return arr


if __name__ == "__main__":
	# some tests
	lst1 = [2, 1, 34, 3, 6, 2, 4, 7]
	print(heap_sort(lst1) == [1, 2, 2, 3, 4, 6, 7, 34])
	lst2 = []
	print(heap_sort(lst2) == [])
	lst3 = [1]
	print(heap_sort(lst3) == [1])
	lst4 = [2, 1]
	print(heap_sort(lst4) == [1, 2])
	lst5 = [1, 2, 3]
	print(heap_sort(lst5) == [1, 2, 3])