# Insertion sort is a simple sorting algorithm that works similar to the 
# way you sort playing cards in your hands. The array is virtually split 
# into a sorted and an unsorted part. Values from the unsorted part are 
# picked and placed at the correct position in the sorted part

def insertion_sort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]
        while search_index > 0 and unsorted_list[search_index-1] > insert_value :
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1
            unsorted_list[search_index] = insert_value
            # print(unsorted_list)

    print(unsorted_list)

arr = [50, 40, 30, 20, 10]
insertion_sort(arr)




# def insertionSort(arr):
#   # Start from 1 as arr[0] is always sorted
#   for i in range(1, len(arr)): 
#     currentElement = arr[i]
#     # Move elements of arr[0..i-1], that are greater than key, 
#     # to one position ahead of their current position
#     j = i-1
#     while j >= 0 and arr[j] > currentElement :
#         arr[j + 1] = arr[j]
#         j -= 1
#      # Finally place the Current element at its correct position.
#     arr[j + 1] = currentElement
# # Driver code to test above
# arr = [9, 6, 7, 2, 5, 8]
# insertionSort(arr)
# for i in range(len(arr)):
#   print ("% d" % arr[i])