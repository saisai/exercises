package main

import "fmt"

func main() {

    countries := map[string]string{
        "sk": "Slovakia",
        "ru": "Russia",
        "de": "Germany",
        "no": "Norway",
    }

    for country := range countries {
	    fmt.Println(country, "=>", countries[country])
    }

    for key, value := range countries {
	    fmt.Printf("countries[%s] = %s\n", key, value)
    }
    
  }
 

