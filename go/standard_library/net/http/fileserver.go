package main

import (
	"log"
	"net/http"
)

func main() {
	log.Fatal(http.ListenAndServe(":8888", http.FileServer(http.Dir("/tmp"))))
}

