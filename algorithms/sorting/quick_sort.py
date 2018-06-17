def quick_sort(arr):
	left = 0
	right = len(arr) - 1
	return quick_sort_helper(arr, left, right)

def partition(arr, left, right):
    pivot = arr[right]
    left_wall = left - 1
    for current_index in range(left, right):
    	if arr[current_index] <= pivot:
    		left_wall += 1
    		arr[current_index], arr[left_wall] = arr[left_wall], arr[current_index]
    arr[left_wall + 1], arr[right] = arr[right], arr[left_wall + 1]
    return left_wall + 1

def quick_sort_helper(arr, left, right):
	if len(arr) < 2:
		return arr
	if left < right:
		q = partition(arr, left, right)
		quick_sort_helper(arr, left, q - 1)
		quick_sort_helper(arr, q + 1, right)
		return arr

if __name__ == "__main__":
	# some tests
	lst1 = [2, 1, 34, 3, 6, 2, 4, 7]
	print(quick_sort(lst1) == [1, 2, 2, 3, 4, 6, 7, 34])
	lst2 = []
	print(quick_sort(lst2) == [])
	lst3 = [1]
	print(quick_sort(lst3) == [1])
	lst4 = [2, 1]
	print(quick_sort(lst4) == [1, 2])
	lst5 = [1, 2, 3]
	print(quick_sort(lst5) == [1, 2, 3])
	lst6 = [2, 1, 34, 3, 6, 2, 4, 7, 5, 6, 6, 89, 2]
	print(quick_sort(lst6) == [1, 2, 2,2, 3, 4, 5, 6, 6, 6, 7, 34, 89])