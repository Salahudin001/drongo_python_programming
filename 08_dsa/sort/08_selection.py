# The selection sort algorithm begins by finding the smallest element in the list and interchanges it with the data stored at the first 
# position in the list

def selection_sort(unsorted_list):
    size_of_list = len(unsorted_list)
    for i in range(size_of_list):
        small = i
        for j in range(i+1, size_of_list):
            if unsorted_list[j] < unsorted_list[small]:
                small = j
        temp = unsorted_list[i]
        unsorted_list[i] = unsorted_list[small]
        unsorted_list[small] = temp
        print(unsorted_list)


a_list = [3, 2, 35, 4, 32, 94, 5, 7]
print("List before sorting", a_list)
selection_sort(a_list)
print("List after sorting", a_list)


# Selection sort in Python
 
# def selectionSort(arr):
 
#    # loop to iterate over the array elements
#    for i in range(len(arr)):
   
#        # set min_index equal to the first unsorted element
#        min_index = i
 
#        # iterate over unsorted sublist
#        for j in range(i+1, len(arr)):
 
#     #helps in finding the minimum element
#            if arr[min_index] > arr[j]:
#                min_index = j
           
#        # swapping the minimum element with the element at min_index to place it at its correct position
     
#        arr[i], arr[min_index] = arr[min_index], arr[i]