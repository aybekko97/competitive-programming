
def fact(n, mod):
    f = 1
    for i in range(1, n + 1):
        f = (f * i) % mod
    return f


def modular_multiplicative_inverse(a, p):
    """
    Article about modular multiplicative inverse
    https://blogarithms.github.io/articles/2019-01/fermats-theorem
    """

    def bin_exp(x, y, mod):
        """
        Errichto's tutorial about Binary Exponentiation
        https://www.youtube.com/watch?v=L-Wzglnm4dM
        """
        res = 1
        while y > 0:
            if y % 2 == 1:
                res = (res * x) % mod
            x = (x * x) % mod
            y //= 2
        return res

    return bin_exp(a, p - 2, p)


def main():
    mod = int(1e9) + 7

    a = 34
    b = 14

    # find (a! / b!) % mod, where x! means factorial of x
    # let's calculate factorials modulo mod
    f_a = fact(a, mod)
    f_b = fact(b, mod)

    # (f_a / f_b) % MOD == (f_a * modular_multiplicative_inverse(f_b, mod)) % mod
    f_b_inverse = modular_multiplicative_inverse(f_b, mod)

    res = (f_a * f_b_inverse) % mod
    print(res)


if __name__ == "__main__":
    main()
