def is_happy_number(n) -> bool:
    slow_ptr = n
    fast_ptr = sum_of_squared_digits(n)

    while fast_ptr != slow_ptr:
        slow_ptr = sum_of_squared_digits(slow_ptr)
        fast_ptr = sum_of_squared_digits(sum_of_squared_digits(fast_ptr))

    return fast_ptr == 1


def sum_of_squared_digits(n: int) -> int:
    digit_sum = 0

    while n > 0:
        digit_sum += (n % 10) ** 2
        n = n // 10

    return digit_sum


if __name__ == "__main__":
    inputs = [28, 4]
    for input in inputs:
        print(f"num={input}, is_happy_num: {is_happy_number(input)}")
