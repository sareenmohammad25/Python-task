

# Task 1A: Fix `addup1A`
def addup1A(upper_limit):
    counter = 1
    total = 0
    while counter <= upper_limit:
        total = total + counter
        counter = counter + 1
    return total

# Task 1B: Fix `addup1B`
def addup1B(upper_limit):
    counter = (upper_limit)
    total = 0
    while counter > 0:
        total = total + counter
        counter = counter - 1
    return total

# Task 1C: Fix `addup1C`
def addup1C(upper_limit):
    total = 0
    for counter in range(upper_limit+1):
        total = total + counter
    return total

# Task 1D: Fix `addup1D`
def addup1D(upper_limit):
    if upper_limit > 0:
        return upper_limit + addup1D(upper_limit-1)
    else:
        return 0

### Exercise 2: Generalized `addup` function
    
# MH: 1 + 1 = 2 / 2 points

# Task 2A: Use a for-loop to implement `addup`
def addup2A(numbers):
    total = 0
    for i in numbers:
        total+=i
    return total

# Task 2B: Use a recursion to implement `addup`
def addup2B(numbers):
    if numbers == []:
        return 0
    else:
        return numbers[0] + addup2B(numbers[1:])
    

# Task 3A: Use a while-loop to implement `factorial`
def factorial3A(upper_limit):
    factorial = 1
    counter = upper_limit
    while counter >0:
        factorial*=counter
        counter-=1
    return factorial


# Task 3B: Use a recursion to implement `factorial`
def factorial3B(upper_limit):
    if upper_limit == 0:
        return 1
    else:
        return upper_limit * factorial3B(upper_limit-1)
    

# Task 4A: Implement a function `split` that splits a list into a list of lists of a
# given size
#
def split(l, size):
    """
    This function splits a list `l` into a list of sublists of a given size or smaller,
    if `len(l)` is not a multiple of `size`. 

    Examples
    --------
    >>> split([0, 1, 2, 3, 4, 5, 6, 7], 1)
    [[0], [1], [2], [3], [4], [5], [6], [7]]

    >>> split([0, 1, 2, 3, 4, 5, 6, 7], 2)
    [[0, 1], [2, 3], [4, 5], [6, 7]]

    >>> split([0, 1, 2, 3, 4, 5, 6, 7], 3)
    [[0, 1, 2], [3, 4, 5], [6, 7]]

    Parameters
    ----------
    l : list
        List that will be split into sublists of given size. 

    size : positive integer
        Desired size of sublist (if the input list is not an exact multiple of
        the desired size, the last sublist will be shorter). 

    Returns
    -------
    A list of sublists. 
    """
    # *** Remove comment and 'pass' and insert your program code here ***
    sublist=[]
    for i in range (0,len(l),size):
        sublist.append(l[i:i+size])
    return sublist
    

# Task 4B: Implement a function `join` that joins a list of lists into a single list
#
def join(lists):
    """
    Joins a list of lists into a single list

    Examples
    --------
    >>> join([[1, 2, 3], [3, 2], [1]])
    [1, 2, 3, 3, 2, 1]

    Parameters
    ----------
    lists : list of lists

    Returns
    -------
    A single list obtained by merging all input lists
    """
    # *** Remove comment and 'pass' and insert your program code here ***
    newlit=[]
    for i in lists:
        newlit.extend(i)
    return newlit


#

# Task 5A: Write a function that takes an input list and returns a copy of the input
# list in reverse order. 
#
def reverse(alist):
    """
    Returns a copy of the input list in reverse order.

    Examples
    --------
    >>> lst = [1, 2, 3]
    >>> print(reverse(lst))
    [3, 2, 1]
    >>> print(lst)
    [1, 2, 3]

    Parameters
    ----------
    alist : list
        Input list whose elements should be reversed. 

    Returns
    -------
    A list with items in reverse order. 
    """
    assert type(alist) is list, 'expecting a list'
    a=alist[::-1]
    return a


# Task 5B: Write a function that checks if a list is a palindrome.  
#
def is_palindromic(alist):
    """
    Checks the input list is a palindrome, i.e. if its the same in forward or
    reversed order. If the list is palindromic the return value is 'True', otherwise
    it is 'False'. 

    Examples
    --------
    >>> is_palindromic([1, 2, 1])
    True
    >>> is_palindromic([1, 2, 3, 2])
    False

    Parameters
    ----------
    alist : list
        Input list. 

    Returns
    -------
    A Boolean value indicating if input list is palindromic (True) or not (False). 
    """
    assert type(alist) is list, 'expecting a list'
    return alist == alist[::-1]



