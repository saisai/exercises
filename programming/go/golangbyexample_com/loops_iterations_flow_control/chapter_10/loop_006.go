
package main

import "fmt"

func main() {
	for i := 0; i < 3; i++ {
		fmt.Printf("Outer loop iteration %d\n", i)
		for j := 0; j < 2; j++ {
			fmt.Printf("i = %d j=%d\n", i, j)
		}
	}
}
