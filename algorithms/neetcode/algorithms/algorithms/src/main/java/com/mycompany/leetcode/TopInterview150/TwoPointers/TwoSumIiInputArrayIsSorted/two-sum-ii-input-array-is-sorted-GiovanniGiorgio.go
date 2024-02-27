package main

import "fmt"

func twoSum(nums []int, t int) []int {
	for l, r := 0, len(nums)-1; ; {
		switch {
		case nums[l]+nums[r] > t:
			r--
		case nums[l]+nums[r] < t:
			l++
		default:
			return []int{l + 1, r + 1}
		}
	}

}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Println(twoSum(nums, target))

}
