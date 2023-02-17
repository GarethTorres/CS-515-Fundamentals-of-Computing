# 
# ## CS 515
# ## Homework 3
# 

# ### 1. Conditionals
# 

# (1) Write a function that converts all units of time into seconds.
# The input is a list that indicates [days, hours, minutes, seconds]. 
# The list should at least includes the seconds element, other elements are optional.


def convert_time(alist):    
    """
        Functions to converts time into seconds.

        Examples:
            [5]:     5
            [1,5]:     65
            [1,2,3]:    3723

        Returns: converted seconds.
        
        Parameter: a list
        Precondition: a list has at least one element
    """
    if len(alist) == 1:
        return alist[0]
    elif len(alist) == 2:
        return alist[1] + alist[0] * 60
    elif len(alist) == 3:
        return alist[2] + alist[1] * 60 + alist[0] * 60 * 60
    elif len(alist) == 4:
        return alist[3] + alist[2] * 60 + alist[1] * 60 * 60 + alist[0] * 60 * 60 * 24

        return None

test1 = convert_time([1, 2, 3, 4])
print(test1)


# ### 2. Testing
 
# Here is a function that is not working properly due to the special precondition. 
# Please use unittest.assert_equals() to test the result and indicate what is the problem of this function.
# Then, fix the function so it works correctly!!!
# Use introcs.assert_equals() again to make sure the input qualifies the precondition and test your result again. 
# (consider what n.find(' ') will return if the input is invalid)


def last_name_first(n):
    """
        A single, non-working function.

        The function in this module has a bug (in the sense that it does not satisfy its specification). This allows us to show off debugging.

        Returns: copy of n but in the form 'last-name, first-name'

        Parameter n: the person's name
        Precondition: n is in the form 'first-name last-name'
        with one or more blanks between the two names no spaces in <first-name> or <last-name>
    """

    end_first = n.find(' ')
    beginning_last = n.rfind(' ')
    first = n[:end_first]
    last = n[beginning_last + 1:]
    
    return last+', '+first
test1111 = last_name_first('dirk   nowitki')
print(test1111)

import introcs

def test_last_name_first():

    result = last_name_first('dirk nowitki')
    introcs.assert_equals('nowitki, dirk', result)

    result = last_name_first('dirk   nowitki')
    introcs.assert_equals('nowitki, dirk', result)

test_last_name_first()
print('result correct')

# ### 3. Control Flow

# Function sortnum(). 
# This function takes three numbers as input and sorts the number from small to large (ascending order) 
# and returns the numbers. 
# Using only simple variables and if statements, you should be able to get this to work; 
# a loop is not needed (And SHOULD NOT BE USED!).



def sortnum(alist):
    """ 
        Returns: a list contains three numbers in ascending order. 
        Example: 
        >>>sortnum([2,1,3]) 
        >>>[1,2,3]

        Precondition: alist is a list that contains three numbers. 

    """

    if alist[0] < alist[1] and alist[1] < alist[2]:
        return alist[0:3]
    elif alist[2] < alist[1] and alist[1] < alist[0]:
        return alist[::-1]
    elif alist[1] < alist[0] and alist[0] < alist[2]:
        return [alist[1], alist[0], alist[2]]
    elif alist[0] < alist[2] and alist[2] < alist[1]:
        return [alist[0], alist[2], alist[1]]
    elif alist[1] < alist[2] and alist[2] < alist[0]:
        return [alist[1], alist[2], alist[0]]
    elif alist[2] < alist[0] and alist[0] < alist[1]:
        return [alist[2], alist[0], alist[1]]

        return None


test3 = sortnum([3, 1, 2])
print(test3)


# ### 4. Challenge

# Write a function to anglicize the integers n where 0<n<1000, 
# for example, if the input is 5, the output should be 'five', if the input is 33, 
# the output should be 'thirty three'.



def anglicize(n):
    """
        Functions to anglicize integers in the range 1..999

        The primary function in this module is anglicize(). This is a
        great module to help you understand conditions.

        Examples:
            3:      "three"
            45:     "forty five"
            100:    "one hundred"
            127:    "one hunded twenty seven"
        Returns: English equiv of n.
        
        Parameter: the integer to anglicize
        Precondition: n in 1..999
    """
    if n < 20:
        return anglicize1to19(n)

    elif n < 100:
        return anglicize20to99(n)

    return anglicize100to999(n)


def anglicize1to19(n):
    """
        Returns: English equivalent of n.
        
        Parameter: the integer to anglicize
        Precondition: n in 1..19
    """
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'

    return 'nineteen'


def anglicize20to99(n):
    """
        Returns: English equiv of n.
        
        Parameter: the integer to anglicize
        Precondition: n in 20..99
    """

    return tens(n // 10) + ('' if n % 10 == 0
                               else ' ' + anglicize1to19(n % 10))


def anglicize100to999(n):
    """
        Returns: English equiv of n.
        
        Parameter: the integer to anglicize
        Precondition: n in 100..999
    """
    # Anglicize the first three digits

    hundreds = n % 100
    suffix = ''

    if hundreds > 0 and hundreds < 20:
        suffix = ' ' + anglicize1to19(hundreds)
    elif hundreds > 20:
        suffix = ' ' + anglicize20to99(hundreds)
    
    return anglicize1to19(n//100) + ' hundred' + suffix

def tens(n):
    """
        Returns: tens-word for n
        
        Parameter: the integer to anglicize
        Precondition: n in 2..9
    """
    if n == 2:
        return 'twenty'
    elif n == 3:
        return 'thirty'
    elif n == 4:
        return 'forty'
    elif n == 5:
        return 'fifty'
    elif n == 6:
        return 'sixty'
    elif n == 7:
        return 'seventy'
    elif n == 8:
        return 'eighty'

    return 'ninety'

test22222 = anglicize(786)
print(test22222)

