# O(n*n) = O(n²)
# less efficient time complexity

# Nested for loop
def print_items(n):
    for i in range(n):      # O(n²)
        for j in range(n):
            print(i, j)
    
    for k in range(n):      # O(n)
        print(k)

# Drop Non Dominants
# O(n²) + O(n) = O(n+n²) = O(n²)

print_items(10)