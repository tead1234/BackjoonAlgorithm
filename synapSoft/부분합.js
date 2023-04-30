function solution(sequence, k) {
    var answer = [];
    let ans  = [];
    let ans_idx = [];
    let sum = 0;
    // 시간복잡도가 n2가 걸리니 ... 
    // 부분 배열을 만들고 k보다 작다면 더하고 아니면 뺴는 방식으로
    // 더하고 뺴는 순서 
    let i = 0;
    let minum_length = 9999999;
    let min_idx = 0;
    
    while(i < sequence.length){
        // 시퀸스에서 제일 앞놈을 빼서 넣기
        // 일단 더하고 커지면 뺀다 
        if(ans.length > 0){
                sum = ans.reduce((acc, cur) => {
            return acc + cur;
        });
        
        }else{
            sum =0;
        }
        
        if (sum < k){
            ans.push(sequence[i]);
            ans_idx.push(i);
            i ++;
        }
        else if (sum == k){
            if (ans_idx.length < minum_length){
            answer = [ans_idx.length, ans_idx[0], ans_idx[ans_idx.length-1]];
                    
            }if(ans_idx.length == minum_length && min_idx >= ans_idx[0]){
            answer = [ans_idx.length, ans_idx[0], ans_idx[ans_idx.length-1]];
            }
            min_idx = ans_idx[0];
            minum_length = ans_idx.length;
            ans.push(sequence[i]);
            ans_idx.push(i);
            i ++;
            ans.shift();
            ans_idx.shift();
            }
        
        
        
        else if(sum > k){
            ans.shift();
            ans_idx.shift();
            
        }
    }
    
 
    return [answer[1], answer[2]];
}


// function solution(sequence, k) {
//     const answer = [0, 1000000];
//     let [left, right] = [0, 0];
//     let sum = sequence[0];
//     while(right < sequence.length){
//         if(sum === k){
//             // 길이가 짧은 수열이 여러 개일 경우 대비
//             if(answer[1] - answer[0] > right - left){
//                 answer[0] = left;
//                 answer[1] = right;    
//             }
//             sum -= sequence[left++];
//             sum += sequence[++right];
//         }
//         // 크면 left 증가 >> 수열의 길이를 더 짧게 만들기
//         else if(sum > k) sum -= sequence[left++];
//         // 같으면 right 증가
//         else if(sum < k) sum += sequence[++right];
//     }
//     return answer;
// }
solution([1,1,1,2,3,4,5], 5)