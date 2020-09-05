# Program Purpose:
# Implement a stack that supports the standard stack operations of push(x), pop(), and size().In addition,
# implement a min() method to return the min value of the stack. Using built-in data structures is allowed. 
# Time complexity: all operations should run in O(1). 

# My notes / analyses:
# - going to use the built-in list type
#   Time complexity: https://wiki.python.org/moin/TimeComplexity
# - amortized runtime is acceptable for push(x)
# - With the standard stack operations of push(x) and pop(), there is no way to make min() run in O(1) time. 
#   To get min in O(1), the min value either needs to be at the top of the stack (which conflicts with the 
#   nature of a stack) or it's stored in an instance variable that can be fetched directly. So I created
#   self.min = None in __init__ which should be updated in push and pop. The challenging part is how to update
#   the pop method when the min value is popped, since we need to have the ability to backtrack the min values,
#   not just once, but indefinitly until the stack is popped empty. I found the following algo extremly helpful: 
#   https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
#   and implemented the idea.
# - Overflow concern due to the numeric manipulation to main stack to enable min value backtrack:
#   integer overflow is less of a concern in Python; see
#   https://mortada.net/can-integer-operations-overflow-in-python.html
#   https://www.quora.com/How-is-there-no-integer-overflow-in-Python



class M_Stack():
    """A Stack class that supports push(x), pop(), size(), and min() operation."""
    
    def __init__(self):
        """Inits an instance. 
        
        A M_Stack has two instance variables: a list to store elements and a placeholder to store 
        the min value of the list. The min value gets updated in push and pop methods. """
        self.list = []    # a list 
        self.min = None   # placeholder for the min value
    
    def push(self,x):
        """Pushes the value x to the top of the stack. 
        
        Args:
          x:
            The value to add to the list.
        """

        # if empty list
        if self.min == None:
            # set the min value to x
            self.min = x
            # append x 
            self.list.append(x)
            print(x, "is pushed to the stack")
            
        # if the list is not empty
        else:
            # if the min value is greater than x
            if self.min > x:
                # append (2*x - current min value) to the list
                temp = (2 * x) - self.min
                self.list.append(temp)
                print(x, "is pushed to the stack")
                # update the min value to x
                self.min = x
            # if the min value is smaller than x
            else:
                # no update to the self.min
                # append x to the list
                self.list.append(x)
                print(x, "is pushed to the stack")

    def pop(self):
        """Pops out the value on the top of the Stack."""
        
        # if the list is empty: nothing to pop
        if len(self.list) == 0:
            print("Empty Stack; nothing to pop!")
            
        # if non-empty list
        else: 
            # pop the last element on the list
            popVal = self.list.pop()
            # if the popped value is less than min
            # that means the min value is popped
            if popVal < self.min:
                print(self.min, "is removed")
                # update min value
                self.min = 2*self.min - popVal
            # if the popped value is equal or greater than min
            else:
                # no update to the min value is needed
                print(popVal, "is removed")
    
    def size(self):
        """Returns the number of elements in the Stack."""
        # return the length of the list
        return(len(self.list))
    
    def getMin(self):
        """Returns the min elements in the Stack."""
        if len(self.list) == 0:
            print("Empty Stack!")
        else: 
            return(self.min)  # O(1)
        
    def print(self):
        """Prints the elements in the Stack from the top to the bottom."""
        print("Actual Stack values:\n")
        print("Stack Top")
        # print elements in the list in a reversed order
        for i in self.list[::-1]:
            print(i)
        print("Stack Bottom")
        
# -------------------------------------------------------------------------------------------
# UI

print(
'''
Example for how to interact with the class: 
>>> MS = MinStack()
>>> for i in [8,3,6,3,7,2]:
	MS.push(i)
8 is pushed to the stack
3 is pushed to the stack
6 is pushed to the stack
3 is pushed to the stack
7 is pushed to the stack
2 is pushed to the stack
>>> MS.print()
Actual Stack values:

Stack Top
1
7
3
6
-2
8
Stack Bottom
>>> MS.pop()
2 is removed
>>> MS.pop()
7 is removed
>>> MS.size()
4
>>> MS.getMin()
3
'''
    )
