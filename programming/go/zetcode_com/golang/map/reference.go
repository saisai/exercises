package main

import "fmt"

func main() {

    countries := map[string]string{
        "sk": "Slovakia",
        "ru": "Russia",
        "de": "Germany",
        "no": "Norway",
    }

    countries2 := countries

    countries2["us"] = "USA"

    fmt.Println(countries)
}

