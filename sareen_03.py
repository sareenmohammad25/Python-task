# Exercise 1A: This version of `the_answer` returns the number 42
def the_answerA():
    return 42

# Exercise 1B: This version of `the_answer` prints the number 42
def the_answerB():
    return print(42)

# Exercise 1C: This version of `the_answer` prints the return value of `the_answerA' 
def the_answerC():
    print(the_answerA())

# Exercise 1D: This version of `the_answer` prints the return value of `the_answerB' 
def the_answerD():
    print(the_answerB())



# Exercise 2A: Implement the function `is_divisor`
def is_divisor(a,b):
    if b%a == 0:
        return True
    else:
        return False

# Exercise 2B: Implement the function `test_is_divisor`
def test_is_divisor():
    if is_divisor(3,9) != True:
        return False
    elif is_divisor(2,10) != True:
        return False
    elif is_divisor(4,16) != True:
        return False
    return True

# Exercise 2C: Implement the function `euler1`
def euler1():
    '''returns the sum of all the numbers divisible by 3 or 5 below 1000'''
    total = 0
    counter = 1
    while counter < 1000:
            if is_divisor(3, counter) or is_divisor(5, counter):
                    total = total + counter
            counter = counter + 1
    return total

# Exercise 2D: Implement the function `test_euler1`
def test_euler1():
    if euler1 != 233168:
        return False
    return True

# Exercise 2E: Implement the function `euler1b`
def euler1b(maxvalue):
    total = 0
    counter = 1
    while counter < maxvalue:
            if is_divisor(3, counter) or is_divisor(5, counter):
                    total = total + counter
            counter = counter + 1
    return total

# Exercise 2F: Implement the function `test_euler1b`
def test_euler1b():
    if euler1b(10) != 23:
        return False
    elif euler1b(20) != 78:
        return False
    elif euler1b(1000) != 233168:
        return False
    return True

        

# Exercise 2G: Implement the function `euler1c`
def euler1c(maxvalue,t,f):
    total = 0
    counter = 1
    while counter < maxvalue:
            if is_divisor(t, counter) or is_divisor(f, counter):
                    total = total + counter
            counter = counter + 1
    return total

# Exercise 2H: Implement the function `test_euler1c`
def test_euler1c():
    if euler1c(1000,3,5) != 233168:
        return False
    elif euler1c(1000,3,7) != 214216:
        return False
    elif euler1c(1000,3,6) != 166833:
        return False         
    elif euler1c(200,2,3) != 13167:
        return False
    return True

# Exercise 2I: Implement the function `euler1d`
def euler1d(maxvalue,t,f,k):
    total = 0
    counter = 1
    while counter < maxvalue:
            if is_divisor(t, counter) or is_divisor(f, counter) or is_divisor(k, counter):
                    total = total + counter
            counter = counter + 1
    return total
# Exercise 2J: Implement the function `test_euler1d`
def test_euler1d():
    if euler1d(1000,3,5,7) != 271066:
        return False
    elif euler1d(200,2,3,4) != 13167:
        return False
    return True
