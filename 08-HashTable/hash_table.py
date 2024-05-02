class Hashtable:
    def __init__(self, size = 7): # prime number for hash table (default parameter)
        self.data_map = [None] * size # create a list with 7 'none' spaces

    # ord(letter) ascii number for each letter
    # divide %len(self.data_map) the result number is between 0 and 6 wich is the indexes of the list
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)

        # self.data_map[index] is the list inside the main list
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)): # index 0 to 6
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
        
    for j in list2:
        if j in my_dict:
            return True
    return False


my_hash_table = Hashtable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())

list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))

# print(my_hash_table.get_item('bolts'))
# print(my_hash_table.get_item('washers'))
# print(my_hash_table.get_item('lumber'))

# my_hash_table.print_table()
