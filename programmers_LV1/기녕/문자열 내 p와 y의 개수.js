// 입출력 예 2가지 s와 s2 선언
var s = "pPoooyY"
var s2 = "Pyy"

// 변수들 선언
var list
var arr
var countp
var county

function solution(s){
    list = s.toLowerCase(); // 소문자로 변환
    console.log('list : ', list)
    arr = Array.from(list) // 배열로 변환 
    console.log('arr :', arr)
    countp = arr.filter(element => 'p' === element).length // p개수 셈
    console.log('countp :', countp)
    county = arr.filter(element => 'y' === element).length // y개수 셈
    console.log('county :', county)
    if (countp === county) {
      return true
    }
    else {
      return false
    }

}

console.log(solution(s))