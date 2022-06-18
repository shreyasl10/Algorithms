var http=require('http');
var server=http.createServer(function(req,res){
    console.log("Request was made by "+req.url);
    res.writeHead(200,{'Content-Type':'text/plain'});
    res.end("HELLO WORLD");
});
server.listen(2000,'127.0.0.1')
console.log("Listening to port 2000");