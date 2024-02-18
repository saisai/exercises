package main

import (
  "fmt"
  "log"
  "os/exec"
)

func main() {
  //path, err := exec.LookPath("fortune")
  path, err := exec.LookPath("ls")
  if err != nil {
    log.Fatal("installing fortune is in your future")
  }
  fmt.Printf("fortune is avaialble at %s\n", path)
}
