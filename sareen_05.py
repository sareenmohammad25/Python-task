
from builtins import sum
import math
import requests
import sympy

# Auxiliary function that can be used in Task 2F
def sqrt(n):
    """Returns the square root of an integer (assuming that the input is a square)."""
    assert type(n) is int, 'Expecting integer'
    return int(math.sqrt(n))

# For exercise 3
#
# where to find pi on the web with a precision of 1000 digits after the decimal point
URL_PI = 'http://pi2e.ch/blog/wp-content/uploads/2017/03/pi_dec_1k.txt'

# auxiliary function to be used if you couldn't solve 3A or 3B
def pi_from_sympy(n_fractional=1000):
    """Returns pi in string representation with the desired precision."""
    return str(sympy.N(sympy.pi, n_fractional + 1))


### Exercise 1


# Task 1A
c =299792458
def compute_frequency(wavelength):
    """
    Computes the frequency of a light wave given its wavelength in nanometers (nm).

    Examples
    --------
    >>> compute_frequency(700)
    428274940000000.0

    Parameters
    ----------
    wavelength : float or int > 0
        Wavelength in nanometers. 

    Returns
    -------
    frequency : float
        Frequency of light wave in Hz. 
    """
    assert type(wavelength) in [float, int] and wavelength > 0
    freq = round(c/(wavelength * 1e-9))
    return freq


# Task 1B
#
def print_frequency(wavelength, unit='Hz'):
    """
    Prints the frequency of a light wave given its wavelength. The wavelength is
    assumed to be given in nanometers. An optional unit for the frequency can be
    chosen by setting the second argument (default is 'Hz', supported units are:
    'Hz', 'kHz', 'MHz', 'GHz', and 'THz').

    Examples
    --------
    >>> print_frequency(700, 'THz')
    frequency = 428.3 THz

    Parameters
    ----------
    wavelength : float or int > 0
        Wavelength in nanometers. 

    Returns
    -------
    No return value, prints frequency to standard output.
    """
    assert type(unit) is str
    assert unit in ('Hz', 'kHz', 'MHz', 'GHz', 'THz')
    if(unit == 'Hz'):
        freq = (c/(wavelength * 1e-9))
        print('frequency = {0:.1f} Hz' .format(freq))
    elif(unit == 'kHz'):
        freq = (c/(wavelength * 1e-9))/1e3
        print('frequency = {0:.1f} kHz' .format(freq))
    elif(unit == 'MHz'):
        freq = (c/(wavelength * 1e-9))/1e6
        print('frequency = {0:.1f} MHz' .format(freq))
    elif(unit == 'GHz'):
        freq = (c/(wavelength * 1e-9))/1e9
        print('frequency = {0:.1f} GHz' .format(freq))
    elif(unit == 'THz'):
        freq = (c/(wavelength * 1e-9))/1e12
        print('frequency = {0:.1f} THz' .format(freq))
        

# The following function generates a list of the first n squares by using an infinite
# while loop that is eventually terminated with a break statement. 
#
def squares(n):
    """Returns a list of the first `n` squares."""
    squares = []
    counter = 0
    while True: # start infinite loop
        counter += 1
        if counter > n: # terminate loop as soon as the condition is met
            break
        squares.append(counter ** 2)
    return squares

def squaresA(n):
    """Returns a list of the first `n` squares."""
    # *** Remove comment and 'pass' and insert your program code here ***    
    #code with while loop
    counter=1
    l=[]
    while counter <= n:
        l.append(counter*counter)
        counter+=1
    return l


# Task 2B: Generate a list of squares using a for loop. 
#
def squaresB(n):
    """Returns a list of the first `n` squares."""
    l=[]
    for i in range (1,n+1):
        l.append(i*i)
    return l

# Task 2C: Generate a list of squares using list comprehension. 
#
def squaresC(n):
    """Returns a list of the first `n` squares."""
    return list(i*i for i in range (1,n+1) )

# Task 2D: Generate a list of squares by summing odd numbers. 
#
def squaresD(n):
    """Returns a list of the first `n` squares."""
    pass


# Task 2E: Generate a list of squares recursively. 
#
def squaresE(n):
    """Returns a list of the first `n` squares."""
    if n == 0:
        return []
    return squaresE(n - 1) + [n * n]


# Task 2F: Generate a list of all Pythagorean triples among the first squares. 
#
def pythagorean_triples(n):
    """Lists all Pythagorean triples among the first n squares."""
    l=squares(n)
    p=[]
    for i in range(0,n):
        for j in range(i+1,n):
            if l[i]+l[j] in l:
                p.append((sqrt(l[i]),sqrt(l[j]),sqrt(l[i]+l[j])))
    return p    
        
### Exercise 3

# Task 3A: Read pi from the file available here
# http://pi2e.ch/blog/wp-content/uploads/2017/03/pi_dec_1k.txt
# saved the value as a notepad file named pi_dec_1k.txt
def pi_from_file(filename='pi_dec_1k.txt'):
    handle=open(filename)
    content=handle.read()
    return content

# Task 3B: Retrieve pi from the web using the module requests
#
def pi_from_url(url=URL_PI):
    """Retrieves pi from the web."""
    req=requests.get(url, allow_redirects=True)
    page=req.text
    return page


# Task 3C: Compare pi with math.pi 
# 
def test_pi(pi):
    """Checks if the input string `pi` starts with the constant `math.pi`.
()
    Example
    -------
    >>> test_pi('3.141592653589793')
    True
    >>> test_pi('3.1541592653589792')
    False

    Parameters
    ----------
    pi : str
        High-precision representation of pi stored as a string.

    Returns
    -------
    True if the input string shares the same initial digits with `math.pi`, and False
    otherwise. 
    """
    a=str(math.pi)
    return pi.startswith(a)


# Task 3D: finding peculiar patterns in pi
#   
def find_in_pi(pattern):
    """
    Find a pattern of numbers in the fractional part of pi. Returns the position of
    the pattern if it is contained in the fractional part of pi. Returns -1, otherwise.

    Example
    -------
    >>> find_in_pi('14159')
    0
    >>> find_in_pi('999999')
    761 # Feynman point
    
    Parameters
    ----------
    pattern : str
        Pattern of consecutive numbers represented as a string.

    Returns
    -------
    The lowest index in pi where the pattern is found, and -1 on failure.
    """
    a=pi_from_file()
    if a.find(pattern) == -1:
        return -1
    else:
        return a.find(pattern)-1


# Task 3E: count digits the fractional part of a float
#
def count_digits(number):
    """Counts how often each digit occurs in the fractional part of a floating point
    number. In order to not be limited in precision, the input number is stored as a
    string.

    Example
    -------
    >>> count_digits('10.112223333')
    [0, 2, 3, 4, 0, 0, 0, 0, 0, 0]
    """
    # *** Remove comment and 'pass' and insert your program code here ***
    if '.' in number:
        frac=number.split('.')[1]
    else:
        return 'not a fractional number'
    digit_count=[]
    for i in range(0,10):
        digit_count.append(frac.count(str(i)))
    return digit_count


# Task 3F: print the relative frequency of each digit
#
def print_frequencies(number):
    """Prints the relative frequency of how often each digit occurs in the fractional
    part of the input float number (which is assumed to be represented as a string to
    allow for arbitrary precision). 
    """
    # *** Remove comment and 'pass' and insert your program code here ***
    if '.' in number:
        frac=number.split('.')[1]
    else:
        return 'not a fractional number'
    a=count_digits(number)
    for i in range(0,10):
        b=(a[i]/len(frac))
        print(f'Frequency of {i}: {b:.2%} ')
