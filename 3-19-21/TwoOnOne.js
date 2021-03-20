


let solve = (s1,s2) => [...new Set(s1+s2)].sort().join("");

console.log(solve("loopingisfunbutdangerous", "lessdangerousthancoding"));
console.log(solve("inmanylanguages", "theresapairoffunctions"));