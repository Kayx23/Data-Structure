# Program Purpose: Implement a hash table that hashes using (K mod 15) and 
# resolves collision by linear probing.

# My notes:
# - Primary clustering can drive up the average searching time as we insert more values
# - Possible solution in open addressing: double hashing
# - Good video on primary & secondary clustering: https://youtu.be/e4z493fVGgQ

class HashTable:
    """A HashTable class that has a hash() function, an add(val), and a show() method."""
    
    def __init__(self):
        """Inits an instance of a HashTable, which has an instance variable of a list of 15 None's for placeholder."""
        # initiate a list of 15 None's
        self.arr = [None for i in range(15)]
        
    def H(self,val):
        """Hashes using (K mod 15)."""
        return val % 15
        
    def add(self,val):
        """Add a value to the hash table; resolves collision by linear probing."""
        # hash the value
        h = self.H(val) 
        
        # if no collision 
        if self.arr[h] == None:
            # store the key-value pair (as a tuple) in the regular spot 
            self.arr[h] = (h,val)
        # if collision
        else: 
            # find the next availble spot to store the key-value pair
            index = h
            while self.arr[index] != None:
                index += 1
                # if index points to the last and it still isn't availble
                if index == len(self.arr): 
                    # increase the list size by one
                    self.arr.append(None)
            # now at the next available spot, store the key-value pair here
            self.arr[index] = (h,val)
    
    def show(self):
        """Shows the key-value pairs in the hash table."""
        # prints key-value pairs vertically
        print("(key,value)")
        for i in self.arr:
            print(i)

# -------------------------------------------------------------------------------------------
# UI
print(
'''
Example: 
>>> HT = HashTable()
>>> for i in [62,80,3,6,2,19,36,39,26,78,23,143,1994,713]:
	HT.add(i)
>>> HT.show()
(key,value)
None
None
(2, 62)
(3, 3)
(2, 2)
(5, 80)
(6, 6)
(4, 19)
(6, 36)
(9, 39)
(3, 78)
(11, 26)
(8, 23)
(8, 143)
(14, 1994)
(8, 713)

'''
    )
