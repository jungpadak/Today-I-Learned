function gg(i) {
  console.log(i);
  if (i >= 10) return;
  else gg(i + 1);
}

console.log(gg(0));
