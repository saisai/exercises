package main

import "fmt"

func main() {

	strDict := map[string]string{"Japan":"Tokyo", "China":"Beiging", "Canadan":"Ottawa"}
	for index, element := range strDict {
		fmt.Println("Index :", index, " Element :", element)
	}

	for key := range strDict {
		fmt.Println(key)
	}

	for _, value := range strDict {
		fmt.Println(value)
	}

}

