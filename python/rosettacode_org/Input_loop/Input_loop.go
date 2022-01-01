package main

import (
	"bufio"
	"io"
	"log"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	for {
		s, err := in.ReadString('\n')
		if err != nil {
			// io.EOF is expected, anthing else
			// should be handled/reported
			if err != io.EOF {
				log.Fatal(err)
			}
			break
		}
		// do something with the line of text
		// in string variable s.
		_ = s
	}
}


