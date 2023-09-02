package main

import "fmt"

func main() {

	data := map[string]string{

		"de": "Germany",
		"it": "Italy",
		"sk": "Slovakia",
	}

	for k, v := range data {
		fmt.Println(k, "=>", v)
	}

	fmt.Println("-----------------")

	for k := range data {
		fmt.Println(k, "=>", data[k])
	}
}

