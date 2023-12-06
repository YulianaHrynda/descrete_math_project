def integer_paths():
    pass

def diagonals():
    pass

def parenthesis_sequences(n: int) -> int:
    """
    Returns the amount of possible parenthesis sequences
    of length 2n.

    >>> parenthesis_sequences(3)
    5
    >>> parenthesis_sequences(0)
    0
    >>> parenthesis_sequences(4)
    14
    """
    if not isinstance(n, int) or n < 0:
        return "Wrong input: n has to be >= 0 Try again."
    if n == 0:
        return n

    output = []
    parenthesis = ''
    length = 2*n

    def parenthesis_generator(opening, closing, parenthesis, length, output):
        if opening + closing == length:
            output.append(parenthesis)
        else:
            if opening < length/2:
                parenthesis_generator(opening+1, closing, parenthesis + '(', length, output)
            if closing < opening:
                parenthesis_generator(opening, closing+1, parenthesis + ')', length, output)

    parenthesis_generator(0, 0, parenthesis, length, output)
    return len(output)

def catalan_numbers(n: int, m: int = 1, nums: list = [1, 1]):
    """
    The function that finds the first n Catalan numbers using a recursive formula
    >>> catalan_numbers(10)
    [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]
    """
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]

    if m != n - 1:
        catalan_num = 0
        for k in range(m + 1):
            catalan_num += nums[k] * nums[m - k]
        nums.append(catalan_num)
        m += 1
        return catalan_numbers(n, m, nums)
    else:
        return nums

def catalan_number_formula():
    pass
