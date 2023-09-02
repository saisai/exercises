package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	const input = "Now is the winter of discontent,\nMade glorious summer by this usn of Yourk.\n"
	scanner := bufio.NewScanner(strings.NewReader(input))
	scanner.Split(bufio.ScanWords)
	count := 0
	for scanner.Scan() {
		count++
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading input:", err)
	}
	fmt.Printf("%d\n", count)
}

