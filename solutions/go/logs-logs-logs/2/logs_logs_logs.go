// Package logs: rune exercises.
package logs

import (
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
		if app, ok := appMap[rune]; ok {
			return app
		}
	}

	return "default"
}

// Replace replaces all occurrences of old with new, returning the modified log
// to the caller.
func Replace(log string, oldRune, newRune rune) string {
	result := []rune(log)

	for i, rune := range result {
		if rune == oldRune {
			result[i] = newRune
		}
	}

	return string(result)
}

// WithinLimit determines whether or not the number of characters in log is
// within the limit.
func WithinLimit(log string, limit int) bool {
	return utf8.RuneCountInString(log) <= limit
}
