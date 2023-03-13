def mergeSort(arr):
    if len(arr) > 1:
 
        # Create start ← A[start..mid] and end ← A[mid+1..end]
        mid = len(arr)//2
        start = arr[:mid]
        end = arr[mid:]
 
        # Sort the two halves
        mergeSort(start)
        mergeSort(end)
 
        i = j = k = 0
 
    # Until we reach the end of either start or end, pick larger among
    # elements start and end and place them in the correct position in the sorted array
 
        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                arr[k] = start[i]
                i += 1
            else:
                arr[k] = end[j]
                j += 1
            k += 1
 
    #   When all elements are traversed in either arr1 or arr2,
    #     pick up the remaining elements and put in sorted array
        while i < len(start):
            arr[k] = start[i]
            i += 1
            k += 1
 
        while j < len(end):
            arr[k] = end[j]
            j += 1
            k += 1
 
if __name__ == '__main__':
    arr = [6, 5, 4, 8, 1, 9]
 
    mergeSort(arr)
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()