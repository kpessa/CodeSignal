n = 9;
// m = [0, 1, 3, 6, 2, 7, 13, 20, 12];
m = [0];
let r = x => {
  if (x > m.length - 1) {
    t = r(x - 1) - x > 0 && !m.includes(r(x - 1) - x) ? r(x - 1) - x : r(x - 1) + x;
    m.push(t);
    return t;
  } else {
    return x <= m.length ? m[x] : r(x - 1) - x > 0 ? r(x - 1) - x : r(x - 1) + x;
  }
};
console.log(
  Array(20)
    .fill(0)
    .map((_, i) => r(i))
);
