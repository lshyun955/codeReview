var n = 12345
var str
var arr
var reverseArr

function solution(n) {
  // 숫자열을 문자열로 변환 스프레드 연산자는 문자열을 문자열 변환한다
  str = (n).toString();
  console.log('str :', str)
  arr = [...str]
  console.log('arr :', arr)
  reverseArr = arr.reverse()
  console.log('reverseArr :', reverseArr)
  
  var int = [];
  for (var i = 0; i < reverseArr.length; i++) {
    let r = parseInt(reverseArr[i])
    int.push(r)
  }
  console.log('int :', int)
    return int
}

console.log(solution(n))