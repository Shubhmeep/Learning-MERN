const expressServer = require('express');
const port = 8000;


const app = expressServer();



app.get('/',function(request,response){
    //console.log(request);
    response.send('cool, it is running');
});



app.listen(port,function(err){
    if(err){
        console.log('error',err);

    }
    else{
        console.log("express server is running on port: ",port);
    }
});
