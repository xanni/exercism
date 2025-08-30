// Package parsinglogfiles: regular expression exercises.
package parsinglogfiles

import "regexp"

func IsValidLine(text string) bool {
	re := regexp.MustCompile(`^\[(?:TRC|DBG|INF|WRN|ERR)\]`)
	return re.MatchString(text)
}

func SplitLogLine(text string) []string {
	re := regexp.MustCompile(`<[~*=-]*>`)
	return re.Split(text, -1)
}

func CountQuotedPasswords(lines []string) (count int) {
	re := regexp.MustCompile(`(?i)".*password.*"`)
	for _, line := range lines {
		if re.MatchString(line) {
			count++
		}
	}
	return
}

func RemoveEndOfLineText(text string) string {
	re := regexp.MustCompile(`end-of-line\d+`)
	return re.ReplaceAllLiteralString(text, "")
}

func TagWithUserName(lines []string) []string {
	re := regexp.MustCompile(`User\s+(\S+)`)
	for i, line := range lines {
		if match := re.FindStringSubmatch(line); match != nil {
			lines[i] = "[USR] " + match[1] + " " + line
		}
	}
	return lines
}
