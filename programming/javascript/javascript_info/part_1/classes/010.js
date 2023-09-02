class Article {
  static publisher = "Ilya Kantor";
}

console.log( Article.publisher ); // Ilya Kantor

Article.publisher = "Ilya Kantor test";

console.log( Article.publisher ); // Ilya Kantor