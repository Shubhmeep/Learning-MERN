const Eserver = require('express');
const port = 3000;
const bodyparser = require('body-parser');
const app = Eserver();

app.use(bodyparser.urlencoded({extended:true}));


app.get('/',function(request,response){
    //response.send("Main Calculation Page")
    response.sendFile(__dirname + "/index.html");

});


app.post('/',function(request,response){
    //console.log(request.body)
    var a = Number(request.body.num1);
    var b = Number(request.body.num2);
    var r = a+b;
    response.status(200).send(r.toString());
});

app.listen(port,function(err){
    if(err){
        console.log('error',err);
        

    }
    else{
        console.log("express server is running on port: ",port);
    }
});

