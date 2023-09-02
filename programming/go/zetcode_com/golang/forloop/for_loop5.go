package main

import (
	"fmt"
	"math/rand"
	"time"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

func main() {

	for {

		r := rand.Intn(30)
		fmt.Printf("%d ", r)

		if r == 22 {
			break
		}
	}
}

