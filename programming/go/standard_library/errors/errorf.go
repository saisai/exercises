package main

import "fmt"

func main() {
	const name, id = "bimmler", 17
	err := fmt.Errorf("use %q (id %d) not found", name, id)
	if err != nil {
		fmt.Print(err)
	}
}

