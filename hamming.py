def main():
    print("Hamming Weight of integer {0} is: {1}.".format(9741, hw(9741)))
    print("Hamming Distance of integers {0} and {1} is: {2}.".format(106, 219, hd(106, 219)))


def hw(a):
    """Calculate the Hamming Weight of an input.

    Keyword arguments:
    a -- the input as an integer
    """
    if not isinstance(a, int):
        raise TypeError("Input parameter must be an integer.")

    count = 0
    while a:
        # Source: http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan
        a &= a - 1
        count += 1

    return count


def hd(a, b):
    """Calculate the Hamming Distance of two inputs.

    Keyword arguments:
    a -- the first input as an integer
    b -- the second input as an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Input parameters must be an integer.")

    distance = hw(a ^ b)

    return distance


if __name__ == "__main__":
    main()
