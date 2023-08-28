"""
CS161 | hw2.py
"""
"""
NOTE: DO NOT MODIFY CODE BELOW THIS LINE
"""
num_access_calls = 0
num_swap_calls = 0
def access(a, i):
    """Takes in a list a and an index i as input and returns the identity of the
    character at index i in the list a.
    Parameters
    -----------
    a : list[str]
        The list of characters, each of which is "L", "M", or "R"
    i : int
        The index of the character to be retrieved from a.
    Returns
    -----------
    str
        The character ("L", "M", or "R") at index i in the list a.
    """
    global num_access_calls
    num_access_calls += 1
    if num_access_calls > 3 * len(a):
        raise Exception("More than 3n calls were made to the access function.")
    return a[i]
def swap(a, i, j):
    """ Takes in a list a and two indices i and j as input and swaps the
    elements at those indices.
    Parameters
    -----------
    a : list[str]
        The list of characters, each of which is "L", "M", or "R"
    i : int
        The index of the first character to be swapped.
    j : int
        The index of the second character to be swapped.
    """
    global num_swap_calls
    num_swap_calls += 1
    if num_swap_calls > 6 * len(a):
        raise Exception("More than 6n calls were made to the swap function.")
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
"""
NOTE: DO NOT MODIFY CODE ABOVE THIS LINE
"""
def sortCollection(a):
    """ Takes in a list a of characters, each of which is "L", "M", or "R",
    and sorts the list in place while obeying some special rules (see below).
    Rules:
     - Your code can only access the elements of a by calling the access
    function.
     - Your code can only alter the elements of a by calling the swap function.
     - On a test case of size n, your code cannot call the access function
    more than 6n times or the swap function more than 3n times.
     - While your code can maintain some variables, such as indices of necessary
    elements, it cannot try to store parts of the list in memory.
     - Do not modify the access or swap functions or do anything else that is
     against the spirit of solving the problem in the intended way (e.g.,
    calling a sorting function).
    Parameters
    -----------
    a : list[str]
        The list of characters, each of which is "L", "M", or "R"
    """
    """ BEGIN YOUR CODE HERE """
    
    """ END YOUR CODE HERE """
"""
NOTE: DO NOT MODIFY CODE BELOW THIS LINE
"""
n = int(input())
unsorted = list(input())
sorted = sortCollection(unsorted)
sorted = ''.join(sorted).rstrip('\r\n')
print(sorted, end='')
