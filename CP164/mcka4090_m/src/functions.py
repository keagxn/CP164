"""
-------------------------------------------------------
Midterm Functions
-------------------------------------------------------
Author:  Keagan Mckay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

# Constants
OPERATORS = ('*', '/', '+', '-')


def pq_triage(source, key):
    """
    -------------------------------------------------------
    Removes all values from source that have a priority
    less than key.
    Use: pq_triage(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a key value (?)
    Returns‌​​​​​​‌​:
        None
    -------------------------------------------------------
    """
    counter = 0

    for i in source:
        counter += 1

    for _ in range(counter):

        if source.peek() < key:
            source.remove()

    return


def purge(source, key):
    """
    -------------------------------------------------------
    Finds and removes all values in source that match key.
    Use: purge(source, key)
    -------------------------------------------------------
    Parameters:
        source - a List of values (List)
        key - a data element (?)
    Returns‌​​​​​​‌​:
        None
    -------------------------------------------------------
    """

    for value in source:

        if value == key:
            source.remove(value)

        return


def eval_expression(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = eval_expression(string)
    -------------------------------------------------------
    Parameters:
        string - the space-separted postfix string to evaluate (str)
    Returns‌​​​​​​‌​:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    
    return
