def quick_sort(unsorted_array, first, last):
    if last - first <= 0:
        return
    else:
        partition_point = partition(unsorted_array, first, last)
        quick_sort(unsorted_array, first, partition_point-1)
        quick_sort(unsorted_array, partition_point+1, last)

    
def partition(unsorted_array, first_index, last_index):
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1
    while True:
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1
        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else:
            break
    
    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot
    return less_than_pivot_index

my_array = [43, 3, 77, 89, 4, 20]
print(my_array)
quick_sort(my_array, 0, 5)
print(my_array)

# # finding the partition point & rearranging the array
# def partition(array, low, high):
 
#    # selecting the rightmost element as pivot
#    pivot = array[high];
  
#    # setting the left pointer to point at the lowest index initially
#    left = low;
 
#    #setting the left pointer to point at the lowest index initially
#    right = high - 1;
 
#    #running a loop till left is smaller than right
#    while (left <= right):
#        #incrementing the value of left until the value at left'th
#        # index is smaller than pivot
#        while (array[left] < pivot):
#            left = left + 1
 
#        #decrementing the value of right until the value at right'th
#        #index is greater than pivot
#        while (array[right] > pivot):
#            right = right - 1;
      
#        if (left < right):
#            #swapping the elements at left & right index
#            array[left], array[right] = array[right], array[left]
      
#    #swapping pivot with the element where left and right meet      
#    array[left], array[high] = array[high], array[left]
 
#    # return the partition point
#    return left
 
# # function to perform quicksort
# def quickSort(array, low, high):
#  if low < high:
 
#    # since this function returns the point where the array is
#    #partitioned, it is used to track the subarrays/partitions in the
#    #array
#    pi = partition(array, low, high)
 
#    # recursively calling the function on left subarray
#    quickSort(array, low, pi - 1)
 
#    # recursively calling the function on right subarray
#    quickSort(array, pi + 1, high)