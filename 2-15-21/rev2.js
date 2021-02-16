
//https://www.codewars.com/kata/5a8d1c82373c2e099d0000ac

function solve(strIn, indexA, indexB){
    let newString = strIn.split('');
    if(indexB >= strIn.length)          //B could be larger than our string
        indexB = strIn.length - 1;
    for(let i = 0; i < indexB - indexA + 1; i++)      //A to B inclusive 
        newString[indexA + i] = strIn[indexB - i];
    return newString.join('');
}

console.log(solve("codewars",1,5))  //"cawedors"
console.log(solve("cODEWArs", 1,5))  //"cAWEDOrs"