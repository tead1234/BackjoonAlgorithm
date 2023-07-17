let arr= [1,2,3,4,1,1,3,4];

let targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]];
targets.sort((a,b) => {
    if(a[1] === b[1])
        return a[0] - b[0]
    else{
        return a[1] - b[1]
    }
})

let last = 0;
let ans = 0;
for(let target of targets){
    if(target[0] >= last){
        ans ++ ;
        if(target[1] > last){
            last = target[1];
            
        }
    }
}
console.log(ans);



// bfs 
let dis = [[-1,0], [1, 0], [0, -1], [0, 1]];

// while(arr.length != 0) {
//     let a = arr.shift();
    

//     for(let i = 0; i < 4; i ++ ){
//         let [x,y] = dis[i];
//         console.log(x , y);
        
//         if(a + x + y <= 1 && a + x + y >=0){
//             console.log(a+x + y);
//             arr.push(a+x + y);
//             console.log(arr);
//         }
//     }
// }





// arr.sort((a,b) => a -b);

// console.log(arr);

// const newAr = arr.reduce((map, cur) => {
//     if(map[cur] != undefined){
//         map[cur] += 1;
//     }else{
//         map[cur] = 0;
//     }
//     return map
// }, {});

// console.log(newAr);