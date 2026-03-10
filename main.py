from primePy import primes
from prime_basic_checker import is_prime_basic
# Prime number checker easiest method, counting from 1 to 250
# Call the function to check if 1 is a prime number

def alternative_prime_checker_with_module():
    # Prime number checker using primePy library
    # write numbers into results.txt file
    with open("results_module.txt", "w") as file:
        for number in range(1, 251):
            if primes.check(number):
                file.write(f"{number} is a prime number.\n")
                print(f"{number} is a prime number.")


if __name__ == "__main__": # Entry Point of the Program; the Program only runs if this file is executed directly, not when imported as a module
    print("Prime numbers from 1 to 250 using the basic method:")
    for number in range(1, 251):
        if is_prime_basic(number):
            print(f"{number} is a prime number.")

    print("\nPrime numbers from 1 to 250 using the primePy library:")
    alternative_prime_checker_with_module()
