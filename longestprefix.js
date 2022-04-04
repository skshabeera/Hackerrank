strs=["flowers","flight",]
var longest=function(strs){
    if (strs.length==0){
        console.log( " ")
    }
    for (let i=0;i<strs[0].length;i++){
        for (let j=1;j<strs.length;j++){
            if(strs[0][i]!== strs[j][i]){
                console.log(strs[0])
            }
        }
    }
}