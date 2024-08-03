def my_filter(func, iterable):
    """
    Same as built-in filter() function.

    Args:
        func: A function that takes a single argument and returns a boolean.
        iterable: An iterable containing elements to be filtered by the function.

    Returns:
        A list of filtered items that satisfy the function's condition.
    """
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result
