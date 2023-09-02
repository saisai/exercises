package main

import "fmt"

func main() {

	countries := map[string]string{
		"sk": "Solvakia",
		"ru": "Russai",
		"de": "Germany",
		"no": "Norway",
	}

	fmt.Printf("There are %d pairs in the map\n", len(countries))
}

