package main

import "fmt"

func main() {

	benelux := make(map[string]string)

	benelux["be"] = "Beligum"
	benelux["nl"] = "Netherlands"
	benelux["lu"] = "Luxembourgh"

	fmt.Println(benelux)
	fmt.Printf("%q\n", benelux)
}

