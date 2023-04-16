// 어떤 숫자를 입력했을 떄 
// 그 숫자를 한글로 바꾸고 
// 바꾼 한글의 어절과 글자수를 곱해서 계산하기 
// 숫자를 4단위로 끊고 그 4단위 수에서 위치에 따라 읽기 
var test = ["1원",
    "4원",
    "8원",
    "9,718원",
    "431,409원",
    "459,176,461원"    
];

let dic = new Map();
dic.set('1', '일');
dic.set('2', '이');
dic.set('3', '삼');
dic.set('4', '사');
dic.set('5', '오');
dic.set('6', '육');
dic.set('7', '칠');
dic.set('8', '팔');
dic.set('9', '구');

// 10000000
// [0,4] [4,8]
// console.log(dic.get(1));

// 한글로 어떻게 변형할까 ? 1000원 > 천원 , 1421 4151원 > 천사백이십일만 
// 받아온 금액에서 원 뺴고 ,삭제
for(let tes of test){
    let ans = 0;
    let cnt = 0;
    let cnt2 = 0;
    
    let re = tes.replace('원', '');

    let re2 = re.replaceAll(',','');
    cnt2 = re2.length;
    // console.log("re2", re2);
    let re3 =[];
    // console.log(re2.substr(-1, -4))
    for(let i= re2.length; 0 < i ; i -= 4){
        if(i-4 < 0){
            re3.push(re2.slice(0,i));
        }else
        re3.push(re2.slice(i-4,i));
    }
    for(let re of re3){
        if(re[0] !== '1'){
            cnt ++;
        }
    };
    console.log(cnt + cnt2 + re3.length);
}
// 어절의 수는 re3.length이고 글자수만 따로 계산하면될듯?
// 글자수 = 원래 길이 + ㅇ앞자리가 1이 아닌 것의 갯수 + 원 + 만 + 조 등등

