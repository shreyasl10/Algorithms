var file=require('fs');
var stream=file.createReadStream(__dirname+'/read.txt','utf8');
var i=0;
stream.on('data',function(buffData){
    console.log("Chunk "+i+" of data received:");
    console.log(buffData);
    i+=1;
})