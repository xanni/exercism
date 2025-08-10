// Package logs: rune exercises.
package logs

import (
	"strings"
	"unicode/utf8"
)

var appMap = map[rune]string{
	'☀': "weather",
	'❗': "recommendation",
	'🔍': "search",
}

// Application identifies the application emitting the given log.
func Application(log string) string {
	for _, rune := range log {
		if result := appMap[rune]; result != "" {
			return result
		}
	}

	return "default"
}

// Replace replaces all occurrences of old with new, returning the modified log
// to the caller.
func Replace(log string, oldRune, newRune rune) string {
	var result strings.Builder

	for _, rune := range log {
		if rune == oldRune {
			result.WriteRune(newRune)
		} else {
			result.WriteRune(rune)
		}
	}

	return result.String()
}

// WithinLimit determines whether or not the number of characters in log is
// within the limit.
func WithinLimit(log string, limit int) bool {
	return utf8.RuneCountInString(log) <= limit
}
