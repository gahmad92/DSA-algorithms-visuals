# def binary_search_recursive(arr, target, low=0, high=None, steps=None):
#     if steps is None:
#         steps = []
#     if high is None:
#         high = len(arr) - 1

#     if low > high:
#         steps.append(f"Base case: target {target} not found")
#         return steps, -1

#     mid = (low + high) // 2
#     steps.append(f"Middle index: {mid}, Element: {arr[mid]}")

#     if arr[mid] == target:
#         steps.append(f"Base case: target {target} found at index {mid}")
#         return steps, mid
#     elif arr[mid] < target:
#         steps.append(f"Target {target} > {arr[mid]} -> Search right half")
#         return binary_search_recursive(arr, target, mid + 1, high, steps)
#     else:
#         steps.append(f"Target {target} < {arr[mid]} -> Search left half")
#         return binary_search_recursive(arr, target, low, mid - 1, steps)

# def linear_search(arr, target):
#     steps = []
#     for i, element in enumerate(arr):
#         steps.append(f"Checking index {i}: {element}")
#         if element == target:
#             steps.append(f"Target {target} found at index {i}")
#             return steps, i
#     steps.append(f"Target {target} not found")
#     return steps, -1

# def selection_sort(arr):
#     steps = []
#     for i in range(len(arr)):
#         min_idx = i
#         steps.append(f"Step {i+1}: Current array: {arr}")
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#         steps.append(f"Swapped {arr[i]} with {arr[min_idx]}")
#     steps.append(f"Sorted array: {arr}")
#     return steps, arr

# def merge_sort(arr, steps=None, depth=0):
#     if steps is None:
#         steps = []
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half, steps, depth + 1)
#         merge_sort(right_half, steps, depth + 1)

#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1
#             steps.append(f"Merging: {arr}")

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
#             steps.append(f"Adding remaining left: {arr}")

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
#             steps.append(f"Adding remaining right: {arr}")
#     return steps, arr

# def bubble_sort(arr):
#     steps = []
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#                 steps.append(f"Swapped: {arr}")
#         if not swapped:
#             steps.append(f"No swaps needed. Array is sorted.")
#             break
#     steps.append(f"Sorted array: {arr}")
#     return steps, arr



def binary_search(array, target):
    steps = []  
    low, high = 0, len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        steps.append(f"Low: {low}, High: {high}, Mid: {mid}, Checking: {array[mid]}")

        if array[mid] == target:
            steps.append(f"Found {target} at index {mid}")
            return {"steps": steps, "result": f"{target} found at index {mid}"}
        elif array[mid] < target:
            low = mid + 1
            steps.append(f"Target is greater than {array[mid]}, new low: {low}")
        else:
            high = mid - 1
            steps.append(f"Target is less than {array[mid]}, new high: {high}")

    return {"steps": steps, "result": f"{target} not found"}


def linear_search(array, target):
    steps = []  
    for i, value in enumerate(array):
        steps.append(f"Checking index {i}, value: {value}")
        if value == target:
            steps.append(f"Found {target} at index {i}")
            return {"steps": steps, "result": f"{target} found at index {i}"}
    
    return {"steps": steps, "result": f"{target} not found"}


def selection_sort(array):
    steps = []  
    n = len(array)
    for i in range(n):
        min_index = i
        steps.append(f"Starting with index {i}, current array: {array}")
        
        for j in range(i+1, n):
            steps.append(f"Comparing {array[j]} with {array[min_index]}")
            if array[j] < array[min_index]:
                min_index = j
                steps.append(f"New minimum found at index {min_index}: {array[min_index]}")
        
        array[i], array[min_index] = array[min_index], array[i]
        steps.append(f"Swapped {array[i]} with {array[min_index]}, array now: {array}")
    
    return {"steps": steps, "result": f"Sorted array: {array}"}


def merge_sort(array):
    steps = []  
    
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            steps.append(f"Comparing {left[i]} and {right[j]}")
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def divide(arr):
        if len(arr) <= 1:
            return arr
        middle = len(arr) // 2
        left = divide(arr[:middle])
        right = divide(arr[middle:])
        steps.append(f"Dividing: {arr} into {left} and {right}</br>")
        return merge(left, right)

    sorted_array = divide(array)
    return {"steps": steps, "result": f"Sorted array: {sorted_array}"}


def bubble_sort(array):
    steps = []  
    n = len(array)
    for i in range(n):
        swapped = False
        steps.append(f"Starting pass {i+1}, current array: {array}")
        for j in range(0, n-i-1):
            steps.append(f"Comparing {array[j]} and {array[j+1]}")
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
                steps.append(f"Swapped: {array}")
        if not swapped:
            break
    return {"steps": steps, "result": f"Sorted array: {array}"}
