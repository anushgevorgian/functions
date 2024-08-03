def apply_function(iterable, func):
    """
    Applies the function to each element of the iterable and returns a list of the results.

    Args:
        iterable: An iterable containing elements to be processed by the function.
        func: A function that takes a single argument and returns a value.

    Returns:
        A list of results after applying the function to each item in the iterable.
    """
    result = []
    for item in iterable:
        result.append(func(item))
    return result
