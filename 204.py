def count_prime(n):
    counter = 0
    prime_list = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2,i): # the interval [2,i-1]
            if i%j == 0:   # a prime only divides 1 and itself
                is_prime=False
                break

        if is_prime == True:
            counter+=1
            prime_list+=[i]
    return counter,prime_list



print(count_prime(500))