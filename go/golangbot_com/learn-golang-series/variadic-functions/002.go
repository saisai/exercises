package main

import "fmt"

func change(s ...string) {
	s[0] = "Go"
}

func main() {
	welcome := []string{"Hello", "World"}
	change(welcome...)
	fmt.Println(welcome)
}

