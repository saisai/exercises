
package main

import "fmt"

func sum(xs []float64) float64{
	total :=0.0
	for _, v := range xs {
		total += v
	}
	return total
}

func main() {
	xs := []float64{98, 93, 77, 82, 83}
	fmt.Println(sum(xs))
	fmt.Println(sum[]float64{98,93,77,82,83})
}

