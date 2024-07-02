function solution(cipher, code) {
  let arr = [];
  for (let index = 0; index < cipher.length; index++) {
    if ((index + 1) % code === 0) {
      arr.push(cipher[index]);
    }
  }
  return arr.join("");
}