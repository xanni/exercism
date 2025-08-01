"""Functions to automate Conda airlines ticketing system."""

from __future__ import annotations

from typing import Iterator

SEATING = ("A", "B", "C", "D")
SKIP_ROW = 13


def generate_seat_letters(number: int) -> Iterator[str]:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    for seat in range(number):
        yield SEATING[seat % len(SEATING)]


def generate_seats(number: int) -> Iterator[str]:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    seat_letter = generate_seat_letters(number)
    for seat in range(number):
        row = 1 + seat // len(SEATING)
        if row >= SKIP_ROW:
            row += 1
        yield f"{row}{next(seat_letter)}"


def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers: list[str], flight_id: str) -> Iterator[str]:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        yield f"{seat+flight_id:0<12}"
