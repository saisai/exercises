package main

import (
	"fmt"
	"strconv"
)

func main() {
	i, _ := strconv.Atoi("1234")
	fmt.Println(strconv.Itoa(i + 1))
}

