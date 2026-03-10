from primePy import primes

# Prime number checker easiest method, counting from 1 to 250


def is_prime_basic(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def alternative_prime_checker_with_module():
    # Prime number checker using primePy library
    for number in range(1, 251):
        if primes.check(number):
            print(f"{number} is a prime number.")


if __name__ == "__main__":
    print("Prime numbers from 1 to 250 using the basic method:")
    for number in range(1, 251):
        if is_prime_basic(number):
            print(f"{number} is a prime number.")

    print("\nPrime numbers from 1 to 250 using the primePy library:")
    alternative_prime_checker_with_module()
