package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	if len(os.Args) < 4 {
		fmt.Println("Invalid usage. Please provide MySQL command.")
		return
	}

	// Check if the command starts with "mysql -u" and contains "-p$(./main)"
	if os.Args[0] == "mysql" && os.Args[1] == "-u" && strings.Contains(os.Args[3], "-p$(./main)") {
		password := "ThisIsPassword"
		fmt.Print(password)
	} else {
		fmt.Println("Invalid password")
	}
}
