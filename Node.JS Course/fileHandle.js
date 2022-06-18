var file=require('fs');
file.mkdir('dir',function(){
    file.readFile('read.txt','utf8',function(err,data){
        file.writeFile('./dir/write.txt',data,function(){
            console.log("File copied successfully");
        });
    })
})
file.unlink('./dir/write.txt',function(){
    file.rmdir('dir',function(){
        console.log('Directory removed');
    })
})