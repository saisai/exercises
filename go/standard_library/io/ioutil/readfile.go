package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	content, err := ioutil.ReadFile("readfile.go")
	if err!= nil {
		log.Fatal(err)
	}

	fmt.Printf("File contents : %s", content)
}

