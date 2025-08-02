// Package lasagna: function exercises.
package lasagna

func PreparationTime(layers []string, minutesPerLayer int) int {
	if minutesPerLayer == 0 {
		minutesPerLayer = 2
	}
	return len(layers) * minutesPerLayer
}

func Quantities(layers []string) (noodles int, sauce float64) {
	for _, layer := range layers {
		switch layer {
		case "noodles":
			noodles += 50
		case "sauce":
			sauce += 0.2
		}
	}
	return
}

func AddSecretIngredient(friendsList []string, myList []string) {
	myList[len(myList)-1] = friendsList[len(friendsList)-1]
}

func ScaleRecipe(quantities []float64, portions int) (scaled []float64) {
	for _, quantity := range quantities {
		scaled = append(scaled, quantity*float64(portions)/2)
	}
	return
}
