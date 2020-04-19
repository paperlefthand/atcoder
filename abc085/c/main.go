package main

import (
	"fmt"
)

func main() {
	var n int
	var y int
	fmt.Scan(&n)
	fmt.Scan(&y)

	max5000 := min(n, y/5000)
	max10000 := min(n, y/10000)

	var i, j int
	for i = 0; i <= max10000; i++ {
		for j = 0; j <= max5000-i; j++ {
			if y-10000*i-5000*j == 1000*(n-i-j) {
				fmt.Println(i, j, n-i-j)
				return
			}
		}
	}

	fmt.Println(-1, -1, -1)
	return
}

func min(i, j int) int {
	if i <= j {
		return i
	}
	return j
}
