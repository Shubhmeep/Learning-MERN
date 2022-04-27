//npm init = initialising package.joson file for the server
//package.json = json is js obj notn which is the server config file

const http = require('http');
const port = 8000;


//creating a request handler
function requestHandler(request,response){

    response.end('Response Generated !') // whenever server is started this response will be generated

}



const server = http.createServer(requestHandler); //whenever server is created requestHandler function is called



server.listen(port,function(err){
    if(err){
        console.log(err);
        return;
    }

    else{
        console.log("server is active on port:",port);
    }
})