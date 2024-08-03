def make_counter():
    """
    Returns a function that, when called, increments and returns a counter variable.
    The counter starts at 0 and increments by 1 each time the function is called.

    Returns:
        A function that increments and returns a counter variable.
    """
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter1 = make_counter()
counter2 = make_counter()
print(counter1())
print(counter1())
print(counter2())

