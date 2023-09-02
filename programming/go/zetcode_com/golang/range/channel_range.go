package main

import "fmt"

func main() {

	ch := make(chan int)

	go func() {
		ch <- 5
		ch <- 6
		ch <-7

		close(ch)
	}()

	for n := range ch {
		fmt.Println(n)
	}
}

