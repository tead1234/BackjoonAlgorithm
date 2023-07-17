const fs = require('fs'); // 제출시 삭제 
// const path = './input_boj.txt' // 제출시 삭제 

const readline = require('readline')
const rl = readline.createInterface({
	// input: process.stdin, // 제출시 활성화  
	input: process.stdin, // 제출시 삭제 
	output: process.stdout,
})
let input = []

rl.on('line', function (line) {
	let t = line.split()
	input.push(t)
}).on('close', function () {
  
	// 14681 코드 시작
	console.log(input);
	// 14681 코드 끝
  
	process.exit()
})