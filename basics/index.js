const x = require('./module');
const r = require('./module');
const path = require('path');
const fs = require('fs')


fs.mkdir(path.join(__dirname,'/test'),(err)=>{
    
    if(err){

    console.log(err);
    return

    }

    console.log('done👍')
    
})



x('shubh');
x('zayn')