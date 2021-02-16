
//https://www.codewars.com/kata/5a092d9e46d843b9db000064

let par = list => [...new Set(list)].reduce((a,b)=>a+b);

console.log(par([1, -1, 2, -2, 3])); //3
console.log(par([-3, 1, 2, 3, -1, -4, -2])); //-4
console.log(par([1, -1, 2, -2, 3, 3])); //3