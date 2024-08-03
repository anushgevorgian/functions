def my_zip(*iterables):
    """
    same as built-in zip() function.

    Args:
        *iterables: Multiple iterables to be zipped together.

    Returns:
        A list of tuples with elements from the input iterables.
        Stops zipping when the shortest iterable is exhausted.
    """
    iterators = [iter(it) for it in iterables]
    result = []
    while True:
        try:
            result.append(tuple(next(it) for it in iterators))
        except StopIteration:
            break
    return result
