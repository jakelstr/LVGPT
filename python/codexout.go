package main

import "fmt"

func main() {
	arr := []string{"a", "b", "c", "d", "e"}

	arr = append(arr, "f")

	arr = append(arr, "g")

	fmt.Println(arr)
}
