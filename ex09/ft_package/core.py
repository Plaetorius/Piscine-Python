def count_in_list(lst: list, needle: str) -> int:
    '''Returns the number of occurences of the needle in the list.

    Parameters:
    lst (list): the list where to find the needle occurences
    needle (str): the needle to find in the list

    Returns:
    (int): the number of occurences of needle in lst
    '''
    return lst.count(needle)
