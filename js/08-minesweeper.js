let m = [
  [true, false, false],
  [false, true, false],
  [false, false, false],
];

const directions = [
  [-1, -1],
  [-1, 0],
  [1, 1],
  [0, -1],
  [0, 1],
  [1, -1],
  [1, 0],
  [1, 1],
];

const minesweeper2 = matrix => matrix.map((row, y) => row.map((col, x) => directions.reduce((count, i) => (count += !!(matrix[y + i[0]] && matrix[y + i[0]][x + i[1]])), 0)));

console.log(minesweeper2(m));

function minesweeper(m) {
  a = Array(m.length)
    .fill()
    .map(() => Array(m.length).fill(0));
  for (let r = 0; r < m.length; r++) {
    for (let c = 0; c < m.length; c++) {
      try {
        if (m[r - 1][c - 1]) a[r][c]++;
      } catch {}
      try {
        if (m[r - 1][c]) a[r][c]++;
      } catch {}
      try {
        if (m[r - 1][c + 1]) a[r][c]++;
      } catch {}
      try {
        if (m[r][c + 1]) a[r][c]++;
      } catch {}
      try {
        if (m[r + 1][c + 1]) a[r][c]++;
      } catch {}
      try {
        if (m[r + 1][c]) a[r][c]++;
      } catch {}
      try {
        if (m[r + 1][c - 1]) a[r][c]++;
      } catch {}
      try {
        if (m[r][c - 1]) a[r][c]++;
      } catch {}
    }
  }
  return a;
}
