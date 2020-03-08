var express = require('express')
var app = express()
var path = require('path')
var bodyParser = require('body-parser')
var urlencodedparser = bodyParser.urlencoded({extended:false})

var {getreq} = require('./getroutes')
var {sub} = require('./postroutes')
app.set('view engine','ejs')
app.get('/',getreq);
app.post('/submit',urlencodedparser,sub)


app.listen(process.env.PORT || 9900,()=>{
    console.log('Server on 9900')
})