
package main

import "fmt"

func makeOddGenerator() func() int {
	i := int(1)
	return func() int {
		i += 2
		return i
	}
}

func main() {
	nextOdd := makeOddGenerator()
	fmt.Println(nextOdd())
	fmt.Println(nextOdd())
	fmt.Println(nextOdd())
}

