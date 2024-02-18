package main

import (
  "io"
  "log"
  "os"
  "strings"
)

func main() {
  r := strings.NewReader("some io.Rader stream to be read\n")

  if _, err := io.Copy(os.Stdout, r); err != nil {
    log.Fatal(err)
  }
}
