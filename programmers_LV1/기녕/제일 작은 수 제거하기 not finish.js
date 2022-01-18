
// 코드 실행 통과 채점 X
arr1 = [7,8,6,10,11,19,20,21,4,3,2,1]
arr2 = [10]
let desc
let m = [-1]
function solution(arr) {
  desc = arr.sort(function(a,b){return b - a})
  if (desc.length > 2) {
    desc.pop()
    return desc   
  } else if (desc.length == 1) {
    return m
  }
}

console.log(solution(arr2))

// 코드 실행 통과 채점 X

function solution(arr) {
  if (arr.length > 2) {
      arr.pop()
      return arr
  } else if (arr.length == 1) {
      arr = [-1]
      return arr
  }
}