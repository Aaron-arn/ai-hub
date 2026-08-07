"""Math tools: number theory helpers for gcd, lcm, primes, factorial, fibonacci."""

import math
import sys


def usage():
    print("Usage: python main.py <command> [args]")
    print("Commands:")
    print("  gcd <a> <b> [c ...]          greatest common divisor")
    print("  lcm <a> <b> [c ...]          least common multiple")
    print("  isprime <n>                  primality test")
    print("  primes <n>                   all primes up to n")
    print("  factor <n>                   prime factorization of n (n >= 2)")
    print("  factorial <n>                n!")
    print("  fibonacci <n>                n-th Fibonacci number (1-based)")


def cmd_gcd(args):
    nums = [int(a) for a in args]
    if len(nums) < 2:
        raise ValueError("gcd requires at least two integers")
    result = 0
    for n in nums:
        result = math.gcd(result, n)
    print(result)


def cmd_lcm(args):
    nums = [int(a) for a in args]
    if len(nums) < 2:
        raise ValueError("lcm requires at least two integers")
    result = 1
    for n in nums:
        result = result * n // math.gcd(result, n)
    print(result)


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def primes_up_to(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, ok in enumerate(sieve) if ok]


def factorize(n):
    if n < 2:
        raise ValueError("factor requires n >= 2")
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def fibonacci(n):
    if n < 1:
        raise ValueError("fibonacci requires n >= 1")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def main():
    args = sys.argv[1:]
    if not args:
        usage()
        sys.exit(1)
    command = args.pop(0)
    try:
        if command == "gcd":
            cmd_gcd(args)
        elif command == "lcm":
            cmd_lcm(args)
        elif command == "isprime":
            n = int(args[0])
            print("True" if is_prime(n) else "False")
        elif command == "primes":
            n = int(args[0])
            print(" ".join(str(p) for p in primes_up_to(n)) if n >= 2 else "")
        elif command == "factor":
            print(" ".join(str(f) for f in factorize(int(args[0]))))
        elif command == "factorial":
            print(math.factorial(int(args[0])))
        elif command == "fibonacci":
            print(fibonacci(int(args[0])))
        else:
            raise ValueError(f"unknown command: {command}")
    except (ValueError, IndexError) as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
