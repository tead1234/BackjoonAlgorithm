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
            }
        
        
        
        else if(sum > k){
            ans.shift();
            ans_idx.shift();
            
        }
    }
    
 
    return [answer[1], answer[2]];
}

solution([1,1,1,2,3,4,5], 5)