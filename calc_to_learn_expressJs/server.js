const Eserver = require('express');
const port = 3000;

const app = Eserver();


app.get('/',function(request,response){
    response.send("Main Calculation Page")
});
app.listen(port,function(err){
    if(err){
        console.log('error',err);

    }
    else{
        console.log("express server is running on port: ",port);
    }
});

