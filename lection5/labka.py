def factorial(n):
    if n == 0:
        return 1
    result = n
    for smaller_integer in range(1, n):
        result *= smaller_integer
    return result

#print(factorial(5))


def repeated(n):
    remaining_digits = abs(n)

    while remaining_digits/10 > 1:
        last_digit = remaining_digits % 10
        previous_digit = (remaining_digits // 10) % 10

        if last_digit == previous_digit:
            return True
        remaining_digits = remaining_digits // 10

    return False

print(repeated(50012))