"""
-------------------------------------------------------
Array versions of various sorts.
-------------------------------------------------------
Author: Keagan Mckay
ID:     210924090
Email:  mcka4090@mylaurier.ca
__updated__ = "2022-04-14"
-------------------------------------------------------
"""


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of array-based sort operations.
    -------------------------------------------------------
    """
    # The Sorts

    @staticmethod
    def radix_string_sort(strings):
        """
        -------------------------------------------------------
        Performs a string radix sort.
        Use: Sorts.radix_string_sort(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns‌‌‌​​​‌​:
            None
        -------------------------------------------------------
        """

        strlen = len(strings)
        srt = []

        if strings == 0:
            strlen = len(max(strings, key=len))

        for ur in range(strlen - 1, -1, -1):
            for cute in strings:
                srt.append(cute)
        return


# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    @staticmethod
    def is_sorted_alpha(strings):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: srtd = Sorts.is_sorted(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns‌‌‌​​​‌​:
            srtd - True if contents of strings are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        n = len(strings)
        i = 0

        while srtd and i < n - 1:

            if strings[i].lower() <= strings[i + 1].lower():
                i += 1
            else:
                srtd = False
        return srtd
