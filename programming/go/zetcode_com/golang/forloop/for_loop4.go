package main

import "fmt"

func main() {

	words := []string{"sky", "cup", "cloud", "news", "water"}

	for idx, word := range words {
		fmt.Printf("%s has index %s\n", word, idx)
	}
}

