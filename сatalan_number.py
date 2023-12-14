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
    '''
    # Make a list of all coords

    all_coords = [[1 if i ==0 or j ==0 else 0 for i in range (n+1)] for j in range(n+1) ]

    for i in range(1,n+1):      #Simulate all possible ways to get to all tilles
        for j in range(1,n+1):
    # If the point is below the diagonal, it has the sum of the paths from the left and above
            if i > j:
                all_coords[i][j] = all_coords[i-1][j] + all_coords[i][j-1]
    # If the point is on the diagonal, it has the same number of paths as the point to the left
            elif i == j:
                all_coords[i][j] = all_coords[i][j-1]
    return all_coords[-1][-1]       # Return the (n,n) ways

def diagonals(n):
    '''
    Returns the number of ways to draw n non-intersecting diagonals in 2n-gon
    >>> diagonals(0)
    0
    >>> diagonals(1)
    1
    >>> diagonals(2)
    0
    >>> diagonals(3)
    14
    >>> diagonals(10)
    58786
    '''
    match n:
        case 0 | 2:
            return 0
        case 1:
            return 1
        case _:

            if n < 0:
                return 'ValueError: Wrong input'

            n += 1
            catalan = [1, 1] +[0 for _ in range(n + 1)]

            for i in range(2, n + 1):
                catalan[i] = 0
                for j in range(i):
                    catalan[i] += catalan[j] * catalan[i-j-1]

            return catalan[n]

def simulate_diagonals(n):
    '''
    Returns the number of ways to draw n non-intersecting diagonals in 2n-gon
    >>> simulate_diagonals(0)
    0
    >>> simulate_diagonals(1)
    1
    >>> simulate_diagonals(2)
    0
    >>> simulate_diagonals(3)
    14
    >>> simulate_diagonals(5)
    132
    '''
    match n:
        case 0 | 2:
            return 0
        case 1:
            return 1
        case _: # n >= 3
            n += 1
        
            def is_valid(used):
                for i in range(len(used)):
                    for j in range(i+1, len(used)):
                        if (min(used[i]) < min(used[j]) < max(used[i]) < max(used[j])) or (min(used[j]) < min(used[i]) < max(used[j]) < max(used[i])):
                            return False
                return True
        
            def count_diagonals(points, used):
                if len(points) < 2:
                    return is_valid(used)
                total = 0
                for i in range(1, len(points)):
                    total += count_diagonals(points[i+1:] + points[1:i], used + [(points[0], points[i])])
                return total
        
            return count_diagonals(list(range(2*n)), [])

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

def generate_catalan_sequence(count):
    def catalan_number(n):
        return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
    catalan_sequence = [catalan_number(i) for i in range(count)]
    return catalan_sequence
