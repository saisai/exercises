package main

import "fmt"
import "time"

func main() {
	fmt.Println("vim-go")
	fmt.Println(time.Now().Format("2006-01-02"))
	fmt.Println(time.Now().Format("Monday, January 2, 2006"))
}
