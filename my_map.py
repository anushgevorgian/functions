def my_map(func, iterable):
    """
    same as built-in map() function.

    Args:
        func: A function that takes a single argument and returns a value.
        iterable: An iterable containing elements to be mapped by the function.

    Returns:
        A list of results after applying the function to each item in the iterable.
    """
    result = []
    for item in iterable:
        result.append(func(item))
    return result
