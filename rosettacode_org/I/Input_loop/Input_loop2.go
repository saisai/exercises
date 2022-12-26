package main

import (
	"bufio"
	"log"
	"os"
)

func main() {
	s := bufio.NewScanner(os.Stdin)
	// select the split function, other ones are avaialbe
	// in bufio or you can provide your own
	s.Split(bufio.ScanWords)
	for s.Scan() {
		// get and use the next 'token'
		asBytes := s.Bytes() // bytes does no allocation
		asString := s.Text() // text returns a newly allocatedstring
		_, _ = asBytes, asString
	}
	if err := s.Err(); err != nil {
		// Handle/report any error (EOF will not be reported)
		log.Fatal(err)
	}
}

