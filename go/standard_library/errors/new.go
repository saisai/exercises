package main

import (
	"errors"
	"fmt"
)

func main() {
	err := errors.New("emit macho dwarf: elf header corrputed")
	if err != nil {
		fmt.Print(err)
	}
}

