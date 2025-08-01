// Package weather: Documentation exercises.
package weather

var (
	// CurrentCondition describes the current weather condition.
	CurrentCondition string
	// CurrentLocation is the location where the forecast is being made.
	CurrentLocation string
)

/*
Forecast takes a city and a condition as input and returns a formatted string
indicating the location and the current weather condition.
*/
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
