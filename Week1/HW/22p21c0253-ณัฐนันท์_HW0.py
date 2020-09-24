#22p21c0253-ณัฐนันท์ 
def quickSort(arr):
	if len(arr) < 2: return arr
	mid = len(arr)//2
	pi = arr[mid]
	arr = arr[:mid] + arr[mid+1:]
	lo=[x for x in arr if x <= pi]
	hi=[x for x in arr if x > pi]

	return quickSort(lo) + [pi] + quickSort(hi)


arr = [23,5,52,23,17,7,2,6,43,34,95,231]
print("Example array: ",end="")
print(arr)

#use quicksort
n = len(arr)
sorted_arr = quickSort(arr)
print("Array after sorted:",sorted_arr)
print("Lowest value:",sorted_arr[0])