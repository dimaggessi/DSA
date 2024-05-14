# Space Complexity: O(n)
# Time Complexity: O(n log n)
#    O(logn) for breaking parts
#    O(n) for putting all together again

# 1) Breaks lists in half
def merge_sort(my_list):
    # 2) Base case: when len(the_list) is 1 ->  break the loop
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index]) # : is a slice operator - not including the mid_index number
    right = merge_sort(my_list[mid_index:])
    return merge(left, right)

# 3) Uses merge() to put lists together
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

# print(merge([1, 2, 7, 8], [3, 4, 5, 6]))

original_list = [3, 1, 4, 2]

sorted_list = merge_sort(original_list)

print('Original List', original_list)

print('\nSorted List:', sorted_list)