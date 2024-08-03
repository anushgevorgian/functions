def get_nth_element(iterable, n):
    """
    Returns the n-th element from the iterable using iter() and next().

    Args:
        iterable: An iterable from which to retrieve the n-th element.
        n: The index of the element to retrieve (0-based).

    Returns:
        The n-th element of the iterable.
    """
    iterator = iter(iterable)
    for i in range(n):
        next(iterator)
    return next(iterator)
