# always start at index of the second element in the list

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

print(insertion_sort([4, 2, 6, 5, 1, 3]))

# for almost sorted list, the time complexity is O(n) not O(n²)