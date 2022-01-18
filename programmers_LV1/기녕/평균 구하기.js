arr1 = [1,2,3,4]
var add = 0

function solution(arr) {
    var len = arr.length
    var answer = 0;
    for (var i = 0; i < arr.length; i++) {
      add += add + arr[i]
    }
    answer = add / len
    
    return answer;
}

solution(arr1)