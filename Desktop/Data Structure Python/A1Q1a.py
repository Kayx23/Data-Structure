# Author: Traky Deng
# Date: Aug 31, 2020
# Assignment question number: Assignment 1, Quesetion 1, Part (a)
# Program Purpose: implement priority queue methods add(x), deleteMin(), and size() using singly linked list 


class Node():
    """A class for the base units in the singly linked list.
    
    The class is called in class SinglyLinkedList and is not to be called on its own. 
    """
    
    def __init__(self,val,NextNode=None):
        """Inits an instance of a Node with a value and optionally a pointer to the next node. 
        
        Args:
          val:
            The value of the node.
          NextNode:
            Optional; a pointer variable pointed to the next node in the singly linked list.
        """
        self.value = val
        self.NextNode = NextNode


class SinglyLinkedList():
    """A singly linked list class that is used to implement a priority queue interface. 
    
    The class offers add(x), deleteMin(), and size() methods. The singly linked list will
    be sorted in an ascending order in the add(x) method, making deleteMin() less expensive. 
    """
    
    def __init__(self,val=None):
        """Inits an instance of a SinglyLinkedList, either empty or with a value as the first node in the list. 
        
        Args:
          val:
            Optional; if not empty, the value would be used to create the first node in the list. 
        """
        self.head = Node(val) if val != None else None
    
    def size(self):
        """Returns a numeric value for the number of elements in the singly linked list."""
        
        # if empty list, returns 0
        if self.head == None:
            return(0)
        
        # if non-empty list, returns the count of nodes 
        else:
            Count = 1 
            # set current node to head node
            CurrentNode = self.head
            # continue to travel down the linked list and count
            while CurrentNode.NextNode != None:
                Count += 1 
                CurrentNode = CurrentNode.NextNode
            # break out of the while loop when current node is at the end of the list
        return(Count)
    
    def add(self,val):
        """Adds a node with value "val" to the singly linked list. 
        
        Note that the add(x) method inserts in a way such that elements in the list are 
        in the ascending order. This makes deleteMin() less expensive. 
        
        Args:
          val:
            The value to be added to the list. 
        """
        
        # if the list is empty
        if self.head == None:
            # create a head node
            self.head = Node(val)
        
        # if the inserted value is smaller than the value of the first node
        elif self.head.value >= val:
            # insert at the head of the list
            k = self.head
            # shift the original head node to the second node
            self.head = Node(val,k)
        
        # if the inserted value is larger than the value of the first node
        # and there is only one node in the list
        elif self.head.value < val and self.head.NextNode == None:
            # make the inserted value the second node
            self.head.NextNode = Node(val)
        
        # if there are more than one node in the list and 
        # need to travel down the list to find the insertion point
        else:
            # use pointers p, q to move from the first node down the list 
            # where q is always one node behind p 
            p = self.head.NextNode; q = self.head
            # continue to travel down the list until the value of the first pointer 
            # is no longer smaller than the value of the node to be inserted 
            while p.value < val:

                # if reaching the end of the list
                if p.NextNode == None:
                    # insert at the end of the list
                    p.NextNode = Node(val)
                    # break out of the function 
                    return None 
                
                # if not reaching the end of the list
                else:
                    # continue to travel
                    q = p
                    p = p.NextNode
            
            # an insersion point is found before the end of the list
            # insert the value and fix the pointer for the existing node
            q.NextNode = Node(val,p)
   
    def deleteMin(self):
        """Deletes the item with the smallest value in the singly linked list."""
        
        # if non-empty list
        if self.head != None:
            # removing the smallest value by resetting the head node 
            self.head = self.head.NextNode
            return None
        
        # if empty list
        else:
            print("Empty List: nothing to delete!")
    
    def print(self):
        """Prints the item values in a singly linked list.
        
        This method was not required by the assignment question, but it provides a method 
        to examine if an element is added, or if the minimal element is removed. 
        """
        
        # let p be a pointer to traverse down the list
        p = self.head
        
        # if the list is not empty, print head node value
        if p != None:
            print(p.value)
            
            # travel down the list and print node values
            while p.NextNode != None:
                p = p.NextNode
                print(p.value)
        
        # if the list if empty
        else:
            print("Empty list!")

# Alias the SinglyLinkedList class using PriorityQueue to hide the implementation
PriorityQueue = SinglyLinkedList

# -------------------------------------------------------------------------------------------
# UI
print(
'''
Author: Traky Deng
Date: Aug 31, 2020
Assignment question number: Assignment 1, Quesetion 1, Part (a)
Program Purpose: Implement priority queue methods add(x), deleteMin(), and size() using singly linked list 

Notes to the Assignment Marker: 
- PriorityQueue() class has been loaded to the environment
- PriorityQueue() class comes with four methods: add(x), deleteMin(), size(), and print(). 
  The first three methods are required by the assignment question while is print() method 
  is an additional method that can be used to check what elements are in the priority queue. 

Example for how to interact with the data structure: 
>>> PQ = PriorityQueue()
>>> PQ.size()
0
>>> PQ.add(55); PQ.add(4); PQ.add(70)
>>> PQ.size()
3
>>> PQ.deleteMin()
>>> PQ.size()
2
>>> PQ.print()
55
70
>>> PQ.deleteMin()
>>> PQ.deleteMin()
>>> PQ.deleteMin()
Empty List: nothing to delete!
'''
    )
