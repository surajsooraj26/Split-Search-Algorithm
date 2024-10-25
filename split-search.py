def split_search(arr, start, end, key): 
    if start > end: 
        return -1 # Indicate that the key is not found 
    mid = (start + end) // 2 
    if arr[start] == key: 
        return start 
    elif arr[end] == key: 
        return end 
    elif arr[mid] == key: 
        return mid 
    left_result = split_search(arr, start + 1, mid - 1, key) 
    right_result = split_search(arr, mid + 1, end - 1, key) 
    if left_result != -1: 
        return left_result 
    elif right_result != -1: 
        return right_result 
    return -1 # Key not found 
arr = [3, 2, -5, 1, 7,9,1,0,6, 8] 
key = int(input("Enter the key to search for: ")) 
result = split_search(arr, 0, len(arr) - 1, key) 
if result != -1: 
    print(f"The element found at index {result}") 
else: 
    print("Element not found")