# def bubble_sort(unordered_list):
#     iteration_number = len(unordered_list)-1
#     for i in range(iteration_number,0,-1):
#         for j in range(i):
#             if unordered_list[j] > unordered_list[j+1]:
#                 temp = unordered_list[j]
#                 unordered_list[j] = unordered_list[j+1]
#                 unordered_list[j+1] = temp


def bubbleSort(arr):
    print(f"before sorting {arr}")
  # loop over array elements
    for i in range(len(arr)):
 
    # loop to compare array elements
        for j in range(0, len(arr) - i - 1):
 
      # compare two adjacent elements
            if arr[j] > arr[j + 1]:
 
        # swap if elements are out-of-order
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        
            print(arr)
    
    # print(f"after sorting {arr}")

arr = [40, 35, 30, 25, 20]
bubbleSort(arr)