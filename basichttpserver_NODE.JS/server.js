//npm init = initialising package.joson file for the server
//package.json = json is js obj notn which is the server config file

const http = require('http');
const port = 8000;
const fs = require('fs'); // built in module in node js used for reading and writting in files
//fs is basically used for file specific operations



// //creating a request handler
// function requestHandler(request,response){
//     response.writeHead(200,{'content-type':'text/html'});
//     fs.readFile('./index.html',function(err,data)
//     {
//         if (err){
//             console.log(err);
//             return response.end("<h1>ERRROR!!!</h1>");
//         }

//         return response.end(data);

//     }
//     );   
//     //readFile() is Asynchronous and readFileSync() is synchronous
// }

function requestHandler(request,response){
        response.writeHead(200,{'content-type':'text/html'});
        let filepath;
        switch(request.url){
            case '/':
                filepath = './index.html';
                break;

            case '/profile':
                filepath = './profile.html';
                break;
            
            default:
                filepath = './err.html';
        }

        fs.readFile(filepath,function(err,data){
            if (err){
                            console.log(err);
                            return response.end("<h1>ERRROR!!!</h1>");
                        }
            return response.end(data);

        });

        //readFile() is Asynchronous and readFileSync() is synchronous
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
