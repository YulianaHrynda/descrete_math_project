'''
Catalan numbers
'''
import math

def count_monotonic_paths(n:int)->int:
    '''
    Counts monotonic paths from (0,0) to (n,n)
    >>> count_monotonic_paths(3)
    5
    >>> count_monotonic_paths(5)
    42
    >>> count_monotonic_paths(9)
    4862
    '''
    all_coords = [[1 if i ==0 or j ==0 else 0 for i in range (n+1)] for j in range(n+1) ]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i < j:
                all_coords[i][j] = all_coords[i-1][j] + all_coords[i][j-1]
            elif i == j:
                all_coords[i][j] = all_coords[i-1][j]
    return all_coords[-1][-1]

def count_triangulations(n):
    '''
    Returns the number of different ways to triangulate a convex polygon with n vertices.
    >>> count_triangulations(3)
    1
    >>> count_triangulations(4)
    2
    >>> count_triangulations(5)
    5
    '''
    if n <= 2:
        return 0
    triangulations = [0] * (n + 1)

    for i in range(4):
        triangulations[i] = 1

    for i in range(4, n + 1):
        for j in range(2, i):
            triangulations[i] += triangulations[j] * triangulations[i - j + 1]

    return triangulations[n]

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
    if n == 0:
        return 1

    output = 0
    parenthesis = ''

    def parenthesis_generator(opening, closing):
        nonlocal output
        if opening + closing == 2*n:
            output += 1
        else:
            if opening < n*2/2:
                parenthesis_generator(opening+1, closing)
            if closing < opening:
                parenthesis_generator(opening, closing+1)

    parenthesis_generator(0, 0)
    return output

def recursive_catalan_numbers(n: int, m: int = 1, nums: list = [1, 1]):
    """
    The function that finds the first n Catalan numbers using a recursive formula
    >>> recursive_catalan_numbers(10)
    [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
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
        return recursive_catalan_numbers(n, m, nums)
    else:
        return nums

def generate_catalan_sequence(count):
    def catalan_number(n):
        return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
    catalan_sequence = [catalan_number(i) for i in range(count)]
    return catalan_sequence
