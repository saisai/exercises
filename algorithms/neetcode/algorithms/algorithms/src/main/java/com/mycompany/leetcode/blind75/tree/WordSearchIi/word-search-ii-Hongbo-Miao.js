const findWords = (board, words) => {
  
  const dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]];
  let res = [];

  const buildTrie = () => {
    const root = {};
    for(const w of words) {
      let node = root;
      for(const c of w) {
        if(node[c] == null) node[c] = {};
        node = node[c];
      }
      node.word = w;
    }
    return root;
  };


  const search = (node, x, y) => {
    if(node.word != null) {
      res.push(node.word);
      node.word = null;
    }

    if(x < 0 || x >= board.length || y < 0 || y >= board[0].length) return;
    if(node[board[x][y]] == null) return;

    const c = board[x][y];
    board[x][y] = "#";
    for(const [dx, dy] of dirs) {
      const i = x + dx;
      const j = y + dy;
      search(node[c], i, j);
    }
    board[x][y] = c; // reset
  };

  const root = buildTrie();
  for(let i = 0; i < board.length; i++) {
    for(let j = 0; j < board[0].length; j++) {
      search(root, i, j);
    }
  }
  return res;
};

const board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]];
const words = ["oath","pea","eat","rain"];

const result = findWords(board, words);

console.log(result);

