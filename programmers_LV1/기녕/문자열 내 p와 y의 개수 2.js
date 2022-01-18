var s = "pPoooyY"
var s2 = "Pyy"
var list
var arr
var countp
var county

function solution(s){
    list = s.toLowerCase();
    console.log('list : ', list)
    arr = Array.from(list)
    console.log('arr : ', arr)
    countp = arr.filter(element => `${arr[0]}` === element).length // arr의 첫번째 값
    console.log('countp : ', countp)
    county = arr.filter(element => `${arr[arr.length -1]}` === element).length // arr의 마지막 값
    console.log('county :', county)
    if (countp === county) {
      return true
    }
    else {
      return false
    }

}

console.log(solution(s2))