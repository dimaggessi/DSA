# proportional = O(n)

# Drop the Constants
# O(n+n) = O(2n) = O(n) 

def print_items(n): #n times
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items(10)