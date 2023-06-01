const fs = require('fs');
const readline = require('readline');

var test = [];
var total = 0;
const readInterface = readline.createInterface({
  input: fs.createReadStream('./test.txt'),
  console: false
});


readInterface.on('line', (line) => {
  test.push(line);
});

readInterface.on('close', () => {

    let dic = new Map();
dic.set('0', '');
dic.set('1', '일');
dic.set('2', '이');
dic.set('3', '삼');
dic.set('4', '사');
dic.set('5', '오');
dic.set('6', '육');
dic.set('7', '칠');
dic.set('8', '팔');
dic.set('9', '구');

let dic2 = ['천', '백', '십', ""];

let dic3 = ["", '만','억','조'];

// dic3.reverse();
for(let tes of test){
    let ans = 0;
    let cnt = 0;
    let cnt2 = 0;
    let re = tes.replace('원', '');
    let re2 = re.replaceAll(',','');
    cnt2 = re2.length;
    let re3 =[];
    for(let i= re2.length; 0 < i ; i -= 4){
        if(i-4 < 0){
            re3.push(re2.slice(0,i));
        }else
        re3.push(re2.slice(i-4,i));
    };
    var answer = [];
    for(let i =0 ; i < re3.length; i ++) {
        let part = re3[i];
        let sub = '';
        for(let j = 0; j < part.length; j ++ ){
            let partOfdic2 = dic2.slice(4 - part.length, 4);
            if(part[j]== '1'){
                // 각 단위벌 마지막 숫자가 1일 경우
                // 일만원 일천원은 안씀 
                if(j == part.length -1){
                    // 마지막 수가 1일때
                    // 1원을 위해서 남기고
                    // 1이지만 1일 안붙이는 경우는 천원 만원일 경우만 그럼
                    // 여기 if에서 만원을 처리해야됨
                    if(i == 1){
                        sub += partOfdic2[j];

                    }else{
                        sub += dic.get(part[j]);
                        sub += partOfdic2[j];
                    }
                    

                }else{
                    sub += partOfdic2[j];
                }
                
            }else if(part[j] == '0'){
                continue;
            }
            else{
 
                sub += dic.get(part[j]);
                sub += partOfdic2[j];
            }
        }
        
        if(sub.length === 0){
            continue;
        }else{
            sub += dic3[i];
            answer.unshift(sub);
        }

        
    }
    // 잘번역되는거 확인했으니 이걸 각 숫자로 바꾸기 
    // 어절은 배열의 length 글자수는 배열의 각 숫자의 길이들의 합 + 1
    let sum = 0;
    for(let a of answer){
        sum += a.length;
    }
    total += (answer.length * (sum+1));
    console.log(tes,answer,"어절",answer.length, "글자수", (sum + 1), "더해지는수", answer.length * (sum+1), "total", total);
}
console.log(total);
});



