"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""

# --------Imports-------- #

# --------Constants-------- #
VOWELS = "aeiouAEIOU"

# --------Question1-------- #


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """

    print(f'Values: {values}')

    i = 0
    temp_list = []

    while i < len(values):

        if values[i] not in temp_list:
            temp_list.append(values[i])

        else:
            values.pop(i)
            i -= 1

        i += 1

    print(f'Cleaned: {values}')

    return

# --------Question2-------- #


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """

    out = ""

    for i in s:

        if i not in VOWELS:
            out += i

    return out

# --------Question3-------- #


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """

    u, l, d, w, r = 0, 0, 0, 0, 0

    for line in fv:
        for c in line:

            if c.isupper():
                u += 1

            elif c.islower():
                l += 1

            elif c.isdigit():
                d += 1

            elif c.isspace():
                w += 1

            else:
                r += 1

    return u, l, d, w, r

# --------Question4-------- #


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """

    if year % 4 == 0:

        if year % 100 == 0:

            if year % 400 == 0:
                leap_year = True

            else:
                leap_year = False

        else:
            leap_year = True

    else:
        leap_year = False

    return leap_year

# --------Question5-------- #


def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """

    s = s.lower()
    s = s.replace(" ", "")

    for i in range(len(s)):

        if s[i] == s[len(s) - 1 - i]:
            palindrome = True

        else:
            palindrome = False

    return palindrome

# --------Question6-------- #


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """

    print(f'Values: {a}')

    md = abs(a[0] - a[1])

    for i in range(len(a) - 1):
        maxdiff = abs(a[i] - a[i+1])

        if maxdiff > md:
            md = maxdiff

    return md

# --------Question7-------- #


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """

    b = []

    for i in range(len(a[0])):
        temp_list = []

        for j in range(len(a)):
            temp_list.append(a[j][i])

        b.append(temp_list)

    return b

# --------Question8-------- #


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """

    small = a[0][0]
    large = a[0][0]

    total = 0
    average = 0

    for lists in a:

        for value in lists:

            if value < small:
                small = value

            elif value > large:
                large = value

            total += value

            average += 1

    average = total / average

    return small, large, total, average

# --------Question8-------- #


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """

    pl = ""

    if word[0].lower() in VOWELS:
        pl = word + 'way'

    else:
        capital = False
        fin = True
        i = 0
        temp_word = ""

        if word[0].isupper():
            capital = True

        while i <len(word) and fin:

            if word[i] in VOWELS:
                fin = False

            else:
                temp_word += word[i].lower()
                i += 1

        pl = word[i:] + temp_word + 'ay'

        if capital:
            pl = pl.capitalize()

    return pl

















