package main

import (
	"fmt"
	"log"
	"math/big"
	"os"
	"strconv"
	"strings"
)

func compile(src string) ([]big.Rat, bool) {
	s := strings.Fields(src)
	r := make([]big.Rat, len(s))
	for i, s1 := range s {
		if _, ok := r[i].SetString(s1); !ok {
			return nil, false
		}
	}
	return r, true
}

func exec(p []big.Rat, n * big.Int, limit int) {
	var q, r big.Int
rule:
	for i := 0; i < limit; i++ {
		fmt.Printf("%d ", n)
		for j := range p {
			q.QuoRem(n, p[j].Denom(), &r)
			if r.BitLen() == 0 {
				n.Mul(&q, p[j].Num())
				continue rule
			}
		}
		break
	}
	fmt.Println()
}

func usage() {
    log.Fatal("usage: ft <limit> <n> <prog>")
}
 
func main() {
    if len(os.Args) != 4 {
        usage()
    }
    limit, err := strconv.Atoi(os.Args[1])
    if err != nil {
        usage()
    }
    var n big.Int
    _, ok := n.SetString(os.Args[2], 10)
    if !ok {
        usage()
    }
    p, ok := compile(os.Args[3])
    if !ok {
        usage()
    }
    exec(p, &n, limit)
}

// ft 15 2 "17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/14 15/2 55/1"
