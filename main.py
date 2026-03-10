from primePy import primes

# Prime number checker easiest method, counting from 1 to 250


def is_prime_basic(num):
    # write numbers into results.txt file
    with open("results_basic.txt", "a") as file:
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        file.write(f"{num} is a prime number.\n")
        return True


def alternative_prime_checker_with_module():
    # Prime number checker using primePy library
    # write numbers into results.txt file
    with open("results_module.txt", "w") as file:
        for number in range(1, 251):
            if primes.check(number):
                file.write(f"{number} is a prime number.\n")
                print(f"{number} is a prime number.")


if __name__ == "__main__":
    print("Prime numbers from 1 to 250 using the basic method:")
    for number in range(1, 251):
        if is_prime_basic(number):
            print(f"{number} is a prime number.")

    print("\nPrime numbers from 1 to 250 using the primePy library:")
    alternative_prime_checker_with_module()
