package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": Vertex{
		40.5692, -74.2536,
	},
	"Google" : Vertex{
		37.1234, -78.2356,
	},
}

func main() {
	fmt.Println(m)
}

