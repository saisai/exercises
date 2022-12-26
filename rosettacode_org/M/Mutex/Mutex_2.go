package main

import (
	"fmt"
	"time"
)

var value int

func slowInc(ch, done chan bool) {
	// channel receive, used here to implement mutex lock.
	// it will block unitl a value is available on the channel
	<-ch

	// same as above
	v := value
	time.Sleep(1e8)
	value = v + 1

	// channel send, equivalent to mutex unlock
	// make a value available on channel
	ch <- true

	// channels can be used to singal completion too

	done <- true

}
func main() {
	ch := make(chan bool, 1)
	done := make(chan bool)
	go slowInc(ch,done)
	go slowInc(ch, done)

	ch <- true
	<-done
	<-done
	fmt.Println(value)
}

