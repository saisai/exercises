package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

func main() {

	http.HandleFunc("/now", logDuration(getTime))
	fmt.Println("Server started at port 8888")
	log.Fatal(http.ListenAndServe(":8888", nil))
}

func logDuration(f func(http.ResponseWriter, *http.Request)) func(http.ResponseWriter, *http.Request) {
	

	return func(w http.ResponseWriter, r *http.Request) {

		start := time.Now()
		f(w, r)
		end := time.Now()
		fmt.Println("The request took", end.Sub(start))
	}
}

func getTime(w http.ResponseWriter, r *http.Request) {

	now := time.Now()
	_, err := fmt.Fprintf(w, "%s", now)

	if err != nil {
		log.Fatal(err)
	}
}

