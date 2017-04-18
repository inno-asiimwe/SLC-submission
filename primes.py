def primes(upperlimit):
    prime_numbers = []
    non_primes = []

    if isinstance(upperlimit, int):
        if upperlimit >= 2:
            for number in range(2, upperlimit+1):
                if number not in non_primes:
                    prime_numbers.append(number)

                    for i in range ( number * number, upperlimit +1, number ):
                        non_primes.append(i)
        else:
            raise ValueError("limit should be greater than 2 ")
    else:
        raise(TypeError, "limit should be  interger")

    return prime_numbers
