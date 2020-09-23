# Program Purpose: Implement an efficient algorithm that determines if two sequences, S1 and S2, contain the same set of elements.
# Note that S1 and S2 can contain duplicates

# My notes on efficiency:
# - one way is to leverage two binary search trees; traverse down tree A and try to find those elements in Tree B.
#   This gives a worst time of O(n^2) when the tree is extremly unbalanced and an avg running time of O(n*log_2(n)).
# - so the hash table in my opinion is a much cleaner way. It does still have a worst time of O(n^2):
#   -- insertion is O(1) on avg; O(n) at worst due to hash collision, which is resolved by open addressing in CPython
#   -- checking length is O(1) since it simply returns __len__
#   -- looking up value is O(1) on avg and O(n) at worst due to collision
# The worst time is not a good measurement in this analysis since the sequence sizes are not large enough to cause significant collision
# that would affect the running time. The average running time is a better measurement, which is O(n). 


def isSameSet(S1,S2):
    """Returns a Boolean value indicating whether two sequences, S1 and S2, contain the same set of elements.
    
    S1 and S2 are expected to be list type.

    Example:
    >>> S1 = [1,3,7,2,5,4,2,1]
    >>> S2 = [7,3,3,4,5,2,1,7]
    >>> isSameSet(S1,S2)
    True
    """

    dict1 = {}
    dict2 = {}


    for i in S1: 
        dict1[i]=1   # 1 is a dummy value

    for i in S2: 
        dict2[i]=1   # 1 is a dummy value
    
    if len(dict1) != len(dict2):
        return False
    
    for i in dict1: 
        # check if the key exists in dict2
        try: 
            dict2[i]

        except KeyError:
            return False

    return True
    
