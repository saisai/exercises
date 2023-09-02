package main

import (
	"fmt"
	"time"
)
func main() {

	location, err := time.LoadLocation("Asia/Bangkok")
	if err != nil {
		panic(err)
	}

	timeInUTC := time.Date(2021, 12, 15, 13, 0, 0, 0, time.UTC)
	fmt.Println(timeInUTC.In(location))
}

