package main

import (
	"fmt"
	"log"
	"os/exec"
)

func main() {
	output, err := exec.Command("ls", "-al").CombinedOutput()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Print(string(output))
}

