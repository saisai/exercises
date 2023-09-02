package main

import (
	"fmt"
	"time"
)

func main() {
	i := 0
	for {
		fmt.Println(i)
		i++
		time.Sleep(time.Second * 1)
	}
}
