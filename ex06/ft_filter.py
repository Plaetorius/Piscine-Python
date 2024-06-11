def ft_filter(function, iterable): 
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    # if not callable(function):
    #     return []
    # filter() has a strang behaviour. When the passed object isn't callable,
    # it returns a 'filter object', which is an iterator. I don't think that
    # we are supposed to reimplement that behaviour, but still, I added that
    # piece of code just in case.
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]

