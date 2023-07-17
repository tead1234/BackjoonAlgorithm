function solution(maps) {
    var answer = [];
    let Map = []
    for(let map of maps){
        let s = map.split("");
        Map.push(s);
    }
    // console.log(Map[0][1]);
    dis = [[-1,0], [1,0 ], [0,-1], [0, 1]];
    // 일단 처음 시작한 부분을 q에 넣음
    q = []
    checkMap = Array.from(Array(Map.length), () => Array(Map[0].length).fill(false));
    // console.log(checkMap);
    // console.log(checkMap);
    for(let i =0; i < Map.length; i ++){
        for(let j =0; j <Map[0].length; j++){
            if(Map[i][j] !== 'X' && checkMap[i][j] === false){
                // 함수 실행
                // total = 0;
                var ans = [];
                ans.push(Map[i][j]);
                checkMap[i][j] = true;
                // q.push([i,j],);
                // total += Number(Map[i][j]);
                q.push([i,j]);
                // 
                while(q.length !== 0){
                    var [a,b] = q.shift();
                    // console.log(a);
                    // ans.push(c);
                    for(let w= 0; w <4 ; w ++){
                        // 좌표를 추가했을떄 
                        var ne_x = dis[w][0] + a;
                        var ne_y = dis[w][1] + b;
                        if (ne_x < Map.length && ne_x >= 0 && ne_y >= 0 && ne_y < Map[0].length){
                            if(checkMap[ne_x][ne_y] === false && Map[ne_x][ne_y] !== 'X'){
                                checkMap[ne_x][ne_y] = true;
                                ans.push(Number(Map[ne_x][ne_y]));
                                q.push([ne_x, ne_y]);
                            }
                        }
                    }
                }
                // answer.push();
                // answer.push(ans[-1]);
                // console.log(ans);
                let lal = 0;
                for(let a of ans){
                    // console.log(lal, a)
                    lal += Number(a);
                }
                answer.push(lal);
                // console.log(lal);
                
                
            }
        }
    }
    if(answer.length === 0){
        return [-1];
    }
    answer.sort();
    console.log(answer);
    return answer;
}

solution(["X591X","X1X5X","X231X", "1XXX1"]);
solution(["XXX","X4X","XXX"]);
solution(["XX4XX","X1X5X","XXXXX", "1XXX1"]);
solution(["XX4","X1X","X3X", "X1X"]);
// solution(["X591X","X1X5X","X231X", "1XXX1"]);