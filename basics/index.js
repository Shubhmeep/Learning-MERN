const x = require('./module');
const r = require('./module');
const path = require('path');
const fs = require('fs')


//make a directory

// fs.mkdir(path.join(__dirname,'/test'),(err)=>{
    
//     if(err){

//     console.log(err);
//     return

//     }

//     console.log('done👍')
    
// })



// x('shubh');    calling the module locally
// x('zayn')




// creating a file

// fs.writeFile(path.join(__dirname,'test','test.js'),'',(err)=>{
//     if(err){
//         throw err

//     }

//     console.log('done')
// })



//read a file

// fs.readFile(path.join(__dirname,'test','test.js'),(err,data) => {
//     if(err){
//         throw err

//     }

//     console.log(data)    BUFFER = // this will not give us data in the file in utf-8 format

// })


// to resolve the BUFFER issue
// fs.readFile(path.join(__dirname,'test','test.js'),(err,data) => {
//     if(err){
//         throw err

//     }
//     const content = Buffer.from(data);
//     console.log(content.toString()) // this will give us data in the file in utf-8 format
    
// })




//let's create a node server

const http = require('http');
const app = http.createServer((req,res) => {
    console.log(req.url);

    if(req.url === '/'){
        fs.readFile(path.join(__dirname,'index.html'),(err,content)=>{
            if(err){
                throw err;
    
            }
    
            res.end(content)
        });
    }else if(req.url === '/about'){
        fs.readFile(path.join(__dirname,'about.html'),(err,content)=>{

            if(err){
                throw err;

            }

            res.end(content)

        })
       
    }
  
})
app.listen(3000,()=>{
    console.log("server running on 3000 port")
})





