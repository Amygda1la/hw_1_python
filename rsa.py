import random

from tabulate import tabulate


def is_prime(n):
    """
    >>> is_prime(2)
      True
    >>> is_prime(11)
      True
    >>> is_prime(8)
      False
    """
    if n <= 1:
        return False
    divider = 2
    while divider <= n // 2:
        if n % divider == 0:
            return False
        divider += 1
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")
    n = p * q
    phi = (p - 1)(q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))


def gcd(A, B):
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while A % B != 0:
        c = A % B
        A = B
        B = c
    return B


def multiplicative_inverse(e, phi):
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    indx, i = 0, 0
    A, B = max(e, phi), min(e, phi)
    A_r, B_r = [A], [B]
    mod_A_B, div_A_B = [A % B], [A // B]
    x, y = [0], [1]
    while mod_A_B[indx] != 0:
        A_r.append(B_r[indx])
        B_r.append(mod_A_B[indx])
        indx += 1
        mod_A_B.append(A_r[indx] % B_r[indx])
        div_A_B.append(A_r[indx] // B_r[indx])
    while len(y) != len(A_r):
        x.append(y[i])
        y.append(x[i] - y[i] * div_A_B[len(div_A_B) - i - 2])
        i += 1
    d = y[-1] % A
    return d


def printing_table_eu(e, phi):
    indx, i = 0, 0
    A, B = max(e, phi), min(e, phi)
    A_r, B_r = [A], [B]
    mod_A_B, div_A_B = [A % B], [A // B]
    x, y = [0], [1]
    while mod_A_B[indx] != 0:
        A_r.append(B_r[indx])
        B_r.append(mod_A_B[indx])
        indx += 1
        mod_A_B.append(A_r[indx] % B_r[indx])
        div_A_B.append(A_r[indx] // B_r[indx])
    while len(y) != len(A_r):
        x.append(y[i])
        y.append(x[i] - y[i] * div_A_B[len(div_A_B) - i - 2])
        i += 1
    table = zip(A_r, B_r, mod_A_B + [None], div_A_B + [None], x[::-1], y[::-1])
    headers = ["A", "B", "A % B", "A // B", "x", "y"]
    print(tabulate(table, headers, tablefmt="pretty"))
