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
