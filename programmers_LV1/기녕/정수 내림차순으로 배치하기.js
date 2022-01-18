var number = 118372
var arr
function solution(n) {
    arr = (n+"").split('');
    arr.sort(function(a,b){return b-a});    
    var answer = Number(arr.toString().replace(/\,/g,''));
    return answer;
}

console.log(solution(number))