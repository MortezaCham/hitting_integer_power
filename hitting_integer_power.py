# This function determines whether the absolute difference between x and y 
def is_hit(x, y, tolerance):
    return tolerance * abs(x-y) <= min(x,y)


def hitting_integer_powers(a, b, tolerance=100):
    # Set initial powers of a and b to 1.
    pa = pb = 1
    # Compute initial values of x and y as a**pa and b**pb, respectively.
    x = a**pa
    y = b**pb
    # Keep looping until the absolute difference between x and y is within the tolerance.
    while not is_hit(x, y, tolerance):
        # If x is smaller than y, increase the power of a and update x.
        if x < y:
            pa += 1
            x *= a
        # If y is smaller than x, increase the power of b and update y.
        else:
            pb += 1
            y *= b
    # When the loop terminates, return the powers pa and pb that we used to get x and y.
    return pa, pb





