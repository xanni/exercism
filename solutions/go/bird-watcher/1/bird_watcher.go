// Package birdwatcher: for loop exercises.
package birdwatcher

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) (sum int) {
	for i := 0; i < len(birdsPerDay); i++ {
		sum += birdsPerDay[i]
	}
	return
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) (sum int) {
	birds := birdsPerDay[(week-1)*7:] // slice of birds in week
	for i := 0; i < 7; i++ {
		sum += birds[i]
	}
	return
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
func FixBirdCountLog(birdsPerDay []int) []int {
	for i := 0; i < len(birdsPerDay); i += 2 {
		birdsPerDay[i]++
	}
	return birdsPerDay
}
