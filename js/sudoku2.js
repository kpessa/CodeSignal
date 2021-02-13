grid = [
  ['.', '.', '.', '1', '4', '.', '.', '2', '.'],
  ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
  ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
  ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
  ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
  ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
  ['.', '.', '.', '5', '.', '.', '.', '7', '.'],
];

function sudoku2(g) {
  let rows = Array(9)
    .fill(0)
    .map(v => new Set());
  let cols = Array(9)
    .fill(0)
    .map(v => new Set());
  let g3x3s = Array(9)
    .fill(0)
    .map(v => new Set());
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (g[i][j] != '.') {
        if (rows[i].has(g[i][j])) return false;
        rows[i].add(g[i][j]);
        if (cols[j].has(g[i][j])) return false;
        cols[j].add(g[i][j]);
        if (g3x3s[3 * Math.floor(i / 3) + Math.floor(j / 3)].has(g[i][j])) return false;
        g3x3s[3 * Math.floor(i / 3) + Math.floor(j / 3)].add(g[i][j]);
      }
    }
  }
  return true;
}

console.log(sudoku2(grid));
