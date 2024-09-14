package main

import (
  "log"
  "net/http"
  "fmt"
)

func main() {
  fmt.Println("hello")
  log.Fatal(http.ListenAndServe(":8888", http.FileServer(http.Dir("/usr/share/doc"))))
}
