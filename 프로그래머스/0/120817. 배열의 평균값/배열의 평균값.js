// function solution(numbers) {
//     var answer = 0;
//     return answer;
// }

const solution = (numbers) => {
    let answer = 0;
    for (let number of numbers) {
        answer += number;
    }
    return answer / numbers.length ;
}