num1 = 11
num2 = num1

print("Before num2 value is update:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22

print("\nAfter num2 value is update:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

print("\nIntegers are immutable, when you put some value in a particular memory space (11)")
print("you cannot change the number value (11)")

dict1 = {'value': 11}
dict2 = dict1

print("\ndict1 and dict2 points to the same object im memory")
print("dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter dict2 value is updated")

print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))