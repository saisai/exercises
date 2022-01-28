package main

import (
	"fmt"
	"math/rand"
)

func main() {
	randloop:
	for {
		switch i := rand.Intn(100); {
		case i % 2 == 0:
			fmt.Printf("Generated even number %d", i)
			break randloop
		}
	}
}

