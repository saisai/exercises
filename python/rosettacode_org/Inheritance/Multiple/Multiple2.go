// example of composition of interfaces.
// Types implement interfaces simply by implemeting functions.
// Thetypedoes not explicitly delare the interfaces it implements.

package main

import "fmt"

// Twointerfaces.

type camera interface {
	photo()
}

type mobilePhone interface {
	call()
}

// compose intefaces. camerPhone interface now contains whatever
// methods are in camera and mobilePhone
type cameraPhone interface {
	camera
	mobilePhone
}

// user defined type.
type htc int


// once the htc type has this method defined ont it, it automatically satisfises
// the camera interface
func (htc) photo() {
	fmt.Println("snap")
}

// add then with this additional method defined, it now satisfies both
// the mobilePhone and cameraPhone interfaces.
func (htc) call() {
	fmt.Println("omg!")
}

func main() {

	// type of i is the composed intefface. The assignmnet only compiles
	// becase static type htc satisfies the interface cameraPhone.
	var i cameraPhone = new(htc)
	// interface functions cab called without reference to the
	// underlying type.
	i.photo()
	i.call()
}

