package main

import "fmt"

func update(a *int, t *string) {
	*a = *a + 5 // deferncing pointer addres
	*t = *t + " Doe" // deferncing pointer addres
	return
}

func main() {

	var age = 20
	var text = "John"
	fmt.Println("Before :", text, age)

	update(&age, &text)

	fmt.Println("After :", text, age)
}

