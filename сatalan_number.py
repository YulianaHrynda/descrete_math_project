def integer_paths():
    pass

def diagonals():
    pass

def parenthesis_sequences():
    pass

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
