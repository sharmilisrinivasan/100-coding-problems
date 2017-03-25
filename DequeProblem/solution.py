'''
File name: solution.py
Author: Sharmili Srinivasan
Date created: 2017-03-25 16:04:26
Date last modified: 2017-03-25 16:12:31
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
    """To read List of int values from user
    
    Returns:
        list: List of int values from user
    """
    in_ = raw_input()
    return [int(float(ele)) for ele in in_.split(" ")]


def split_list_on_value(list_, val_):
    """Splits the given list into list of lists splitting it based
       on element value given (val)
    
    Args:
        list_ (list): List of int values
        val_ (TYPE): Description
    
    Returns:
        List: List of lists of int value split based on the given value
    """
    str_list = " ".join([str(ele) for ele in list_])
    str_list = " " + str_list + " "
    str_list_outputs = str_list.split(" {0} ".format(val_))
    to_return = []
    for str_output in str_list_outputs:
        int_output = [int(float(ele))
                      for ele in str_output.split(" ") if ele]
        if len(int_output) > 0:
            to_return.append(int_output)
    return to_return


def return_alpha(list_):
    """To find the maximum alpha value in the given list
    
    Args:
        list_ (list): List of int values
    
    Returns:
        int: Maximum alpha value
    """
    if len(list_) == 1:
        return list_[0]
    min_ele = min(list_)
    n_ele = len(list_)
    alpha = min_ele * n_ele
    split_lists = split_list_on_value(list_, min_ele)
    for ele_list in split_lists:
        alpha = max(alpha, return_alpha(ele_list))
    return alpha

try:
    no_of_tests = get_int_input()
    output = []
    for test in range(no_of_tests):
        no_ele_in = get_int_input()
        elements = get_str_input()
        output.append(return_alpha(elements))

    for val in output:
        print val
except Exception, e:
    print "Exception:{0}".format(e)
