# factors and prime numbers
number = int(input("Please enter the number : "))

# Checking prime number


def is_prime(number):
    flag = True
    for i in range(2, number):
        if(number % i) == 0:
            flag = False
            break
    return(flag)


# calling the function
checkprime = is_prime(int(number))

# takes an integer argument n and returns a list of all of its factors


def factors(number):
    flist = []
    for i in range(1, number+1):
        if(number % i) == 0:
            flist.append(i)

    return(flist)


flist = factors(number)

# 3.  takes an integer argument n and returns a list of all of its prime factors, that is, the factors which are prime numbers.

# a function named prime_factors


def prime_factors(number):
    primelist = []
    for i in flist:
        if is_prime(i) and i != 1:
            # checking if the number is the prime
            primelist.append(i)

    return(primelist)


print("factors(", number, ")\n", flist)
primelist = prime_factors(number)
print("prime_factors(", number, ")\n", primelist)
