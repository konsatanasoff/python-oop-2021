def get_primes(nums):
    for num in nums:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False

        if is_prime:
            yield num


# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

