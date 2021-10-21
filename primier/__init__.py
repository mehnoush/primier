
# Python program to display all the prime numbers within an interval
# taken from https://www.programiz.com/python-programming/examples/prime-number-intervals


def print_primes(lower, upper):

    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
