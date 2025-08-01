def square_of_sum(number: int) -> int:
    sum_n = (number * (number + 1)) // 2
    return sum_n * sum_n


def sum_of_squares(number: int) -> int:
    return (number * (number + 1) * ((number * 2) + 1)) // 6


def difference_of_squares(number: int) -> int:
    return square_of_sum(number) - sum_of_squares(number)
