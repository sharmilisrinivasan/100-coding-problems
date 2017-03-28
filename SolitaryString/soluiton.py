'''
File name: soluiton.py
Author: SharmiliSri
Date created: 2017-03-28 20:19:32
Date last modified: 2017-03-28 20:45:01
Last modified by: SharmiliSri
Python Version: 2.7
'''


def get_int_input():
    """To read int input from user
    
    Returns:
        int: Input from user
    """
    in_ = raw_input()
    return int(float(in_))


def get_str_input():
    """To read a string from user
    
    Returns:
        str: String read from user
    """
    return raw_input()

try:
    """
    Logic is to
    1. Read the string once and create a hash of
    {character: list of indices of character occurence}
    2. Loop through the hash and find max_val-min_val-1 for each key.
    This gives the maximum distance between two occurences of the same
    character. Ensure, to return -1 if occurence of character is once.

    """
    no_of_tests = get_int_input()
    output = []
    for test in range(no_of_tests):
        current_output = -1
        in_str = get_str_input()
        tmp_hash = {}
        for idx, char in enumerate(in_str):
            if char not in tmp_hash:
                tmp_hash[char] = []
            tmp_hash[char].append(idx)
        for val in tmp_hash.values():
            cal_val = max(val) - min(val) if len(val) != 1 else -1
            current_output = max(current_output, cal_val)
        output.append(current_output - 1 if current_output != -1 else -1)

    for val in output:
        print val
except Exception, e:
    print "Exception:{0}".format(e)
