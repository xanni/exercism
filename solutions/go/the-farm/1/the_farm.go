// Package thefarm: error handling exercises.
package thefarm

import (
	"errors"
	"fmt"
)

var errInvalidCows = errors.New("invalid number of cows")

type InvalidCowsError struct {
	cows    int
	message string
}

func (e *InvalidCowsError) Error() string {
	return fmt.Sprintf("%d cows are invalid: %s", e.cows, e.message)
}

func DivideFood(FodderCalculator FodderCalculator, cows int) (float64, error) {
	var err error
	var factor, fodder float64

	if factor, err = FodderCalculator.FatteningFactor(); err != nil {
		return 0, err
	}

	if fodder, err = FodderCalculator.FodderAmount(cows); err != nil {
		return 0, err
	}

	return factor * fodder / float64(cows), nil
}

func ValidateInputAndDivideFood(FodderCalculator FodderCalculator, cows int) (float64, error) {
	if cows <= 0 {
		return 0, errInvalidCows
	}

	return DivideFood(FodderCalculator, cows)
}

func ValidateNumberOfCows(cows int) error {
	if cows < 0 {
		return &InvalidCowsError{cows: cows, message: "there are no negative cows"}
	}

	if cows == 0 {
		return &InvalidCowsError{cows: cows, message: "no cows don't need food"}
	}

	return nil
}
