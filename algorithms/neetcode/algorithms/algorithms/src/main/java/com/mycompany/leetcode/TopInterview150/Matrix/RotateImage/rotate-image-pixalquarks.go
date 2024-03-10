package main

import "fmt"

func rotate(matrix [][]int) {
	n, m := len(matrix), len(matrix[0])
	for i := 0; i < n; i++ {
		for j := i; j < m; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}

		for j, k := 0, m-1; j < k; j, k = j+1, k-1 {
			matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
		}

	}
}

func main() {
	//matrix := int[][] [[1,2,3],[4,5,6],[7,8,9]]

	matrix := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	rotate(matrix)
	fmt.Println(matrix)

	for _, x := range matrix {
		for _, y := range x {
			fmt.Println(y)
		}
	}
}
