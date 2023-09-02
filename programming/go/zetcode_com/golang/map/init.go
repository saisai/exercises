package main

import "fmt"

func main() {

	var benelux map[string]string

	benelux = make(map[string]string)

	benelux["be"] = "Belgium"
	benelux["nl"] = "Netherlands"
	benelux["lu"] = "Luxembourgh"

	fmt.Println(benelux)
	fmt.Printf("%q\n", benelux)
}

