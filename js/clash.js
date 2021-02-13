s = '80 85 90 100 105 115';
console.log(
  s
    .split(' ')
    .map(item => String.fromCharCode(item))
    .join('')
);
