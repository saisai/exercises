
package main

import (
  "encoding/json"
  "fmt"
  "os"
)

func main() {
  var strings []string
  var jsonstring = `["lorem", "ipsum", "dolor", "sit", "amet"]`

  err := json.Unmarshal([]byte(jsonstring), &strings)

  if err != nil {
    fmt.Println("error while unmarshalling")
    os.Exit(2)
  }

  fmt.Println(strings)

  // convert object to bytes-string
  jsonData, err := json.Marshal(strings)

  if err != nil {
    fmt.Println("error while marshalling")
    os.Exit(2)
  }

  fmt.Println(string(jsonData))
}
