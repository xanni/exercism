// Package sorting: type exercises.
package sorting

import (
	"fmt"
	"strconv"
)

// DescribeNumber should return a string describing the number.
func DescribeNumber(f float64) string {
	return fmt.Sprintf("This is the number %.1f", f)
}

type NumberBox interface {
	Number() int
}

// DescribeNumberBox should return a string describing the NumberBox.
func DescribeNumberBox(nb NumberBox) string {
	return fmt.Sprintf("This is a box containing the number %d.0", nb.Number())
}

type FancyNumber struct {
	n string
}

func (i FancyNumber) Value() string {
	return i.n
}

type FancyNumberBox interface {
	Value() string
}

// ExtractFancyNumber should return the integer value for a FancyNumber
// and 0 if any other FancyNumberBox is supplied.
func ExtractFancyNumber(fnb FancyNumberBox) int {
	if nb, ok := fnb.(FancyNumber); ok {
		if i, err := strconv.Atoi(nb.Value()); err == nil {
			return i
		}
	}

	return 0
}

// DescribeFancyNumberBox should return a string describing the FancyNumberBox.
func DescribeFancyNumberBox(fnb FancyNumberBox) string {
	n := 0
	if fn, ok := fnb.(FancyNumber); ok {
		n = ExtractFancyNumber(fn)
	}
	return fmt.Sprintf("This is a fancy box containing the number %d.0", n)
}

// DescribeAnything should return a string describing whatever it contains.
func DescribeAnything(i any) (desc string) {
	switch v := i.(type) {
	case int:
		desc = DescribeNumber(float64(v))
	case float64:
		desc = DescribeNumber(v)
	case NumberBox:
		desc = DescribeNumberBox(v)
	case FancyNumberBox:
		desc = DescribeFancyNumberBox(v)
	default:
		desc = "Return to sender"
	}
	return
}
