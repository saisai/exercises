package main

import "fmt"

func main() {
	// first task
    printSearchForward("soap")
    printSearchForward("gold")
    printSearchForward("fire")
    // extra task
    printSearchReverseMult("soap")
    printSearchReverseMult("gold")
    printSearchReverseMult("fire")

}

// First task solution uses panic as an exception-like mechanism, as requested
// by the task.  Note however, this is not idiomatic in Go and in fact
// is considered bad practice.
func printSearchForward(s string) {
	fmt.Printf("Forward search: %s: ",s )
	defer func() {
		if x := recover(); x != nil {
			if err, ok := x.(string); ok && err == "no match" {
				fmt.Println(err)
				return
			}
			panic(x)
		}
	}()
	fmt.Println("smallest index = ", searchForwardPanic(s))
}

func searchForwardPanic(s string) int {
	for i, h := range haystack {
		if h == s {
			return i
		}
	}
	panic("no math")
	return -1
}

// Extra task, a quirky search for multiple occurrences.  This is written
// without panic, and shows more acceptable Go programming practice.
func printSearchReverseMult(s string) {
	fmt.Printf("Reverse search for multiples: %s: ", s)
	if i := searchReverseMult(s); i > - 1 {
		fmt.Println("largest index = ", i)
	} else {
		fmt.Println("no multiple occurrence")
	}
}

func searchReverseMult(s string) int {
	largest := -1
	for i := len(haystack) - 1; i >= 0; i-- {
		switch {
		case haystack[i] != s:
		case largest == -1:
			largest = i
		default:
			return largest
		}
	}
	return -1
}
