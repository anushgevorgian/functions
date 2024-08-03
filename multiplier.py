def make_multiplier_of(n):
    """
    Takes an integer n and returns a function that multiplies its argument by n.

    Args:
        n: An integer by which the returned function will multiply its argument.

    Returns:
        A function that multiplies its argument by n.
    """

    def multiplier(x):
        return x * n

    return multiplier



multiplier_of_3 = make_multiplier_of(3)
print(multiplier_of_3(10))

