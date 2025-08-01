"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # Number of minutes per layer


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """Calculare the preparation time required based on the number of layers.

    :param number_of_layers: int - number of layers in the lasanga.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers in the lasagna as an argument and
    returns how many minutes will be required to prepare that many layers based
    on the `PREPARATION_TIME`.
    """

    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the elapsed time.

    :param number_of_layers: int - number of layers in the lasanga.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time (in minutes) spent cooking so far.

    Function that takes the number of layers in the lasagna and the actual
    minutes the lasagna has been in the oven as arguments and returns how many
    total minutes have elapsed so far based on the `PERPARATION_TIME`.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
