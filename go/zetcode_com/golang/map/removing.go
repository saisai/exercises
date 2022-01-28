package main

import "fmt"

func main() {

    countries := map[string]string{
        "sk": "Slovakia",
        "ru": "Russia",
        "de": "Germany",
        "no": "Norway",
    }

    fmt.Println(countries)

    delete(countries, "ru")

    fmt.Println(countries)
}

