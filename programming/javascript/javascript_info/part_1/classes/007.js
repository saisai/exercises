class Button {
  constructor(value) {
    this.value = value;
  }

  click(test) {
    console.log(this.value + " : " + test);
  }
}

let button = new Button("hello");

setTimeout(() => button.click("world"), 1000);

//setTimeout(button.click, 1000); // undefined