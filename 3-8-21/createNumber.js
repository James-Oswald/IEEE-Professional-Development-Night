

//let createNumber=n=>"("+n[0]+n[1]+n[2]+") "+n[3]+n[4]+n[5]+"-"+n[6]+n[7]+n[8]+n[9];
//let createNumber=(n)=>n.splice(0,0,"(").splice(4,0,") ").splice(9,0,"-").join("");

/*
function createNumber(n,i=[0,4,5,9],c="() -"){
    return i.map((_,j)=>n.splice(i[j],0,c[j])), n;
}*/

let createNumber1=n=>"("+n[0]+n[1]+n[2]+") "+n[3]+n[4]+n[5]+"-"+n[6]+n[7]+n[8]+n[9];
let createNumber2=(n,i=[0,4,5,9],c='() -')=>(i.map((_,j)=>n.splice(i[j],0,c[j])),n.join(''));
let createNumber3=(n,c='(xxx) xxx-xxxx')=>(n.map(j=>c=c.replace('x',j)),c);
let createNumber4=n=>(c='(xxx) xxx-xxxx',n.map(j=>c=c.replace('x',j)),c);
let createNumber5=n=>eval("c='(xxx) xxx-xxxx',n.map(j=>c=c.replace('x',j)),c");

//let createNumber=(n,a=)=>;

console.log(createNumber5([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) //"(123) 456-7890"

