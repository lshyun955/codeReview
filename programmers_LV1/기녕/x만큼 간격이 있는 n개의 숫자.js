var x = 2
var n = 5
var a = 0

function solution(x, n) {
    var answer = [];
    for (var i = 0; i < n; i++ ) {
      a += x
      answer.push(a)
      console.log(a)      
    }
    return answer;
}

console.log(solution(x, n))

//// 프로그래머스 제출 답안 
// var a = 0
// function solution(x, n) {
//     var answer = [];
//     for (var i = 0; i < n; i++) {
//         a += x
//         answer.push(a)
//     }
//     return answer;
// }