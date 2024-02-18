package main

import "fmt"

func canCompleteCircuit(gas []int, cost []int) int {
	n := len(gas)
	fueLeft, globalFuelLeft, start := 0, 0, 0
	for i := 0; i < n; i++ {
		globalFuelLeft += gas[i] - cost[i]
		fueLeft += gas[i] - cost[i]
		if fueLeft < 0 {
			start = i + 1
			fueLeft = 0
		}
	}

	if globalFuelLeft < 0 {
		return -1
	}
	return start
}

func main() {
	gas := []int{1, 2, 3, 4, 5}
	cost := []int{3, 4, 5, 1, 2}
	result := canCompleteCircuit(gas, cost)
	fmt.Println(result)
}
