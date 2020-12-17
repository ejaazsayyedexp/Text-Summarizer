var express = require('express')
var app = express()
var path = require('path')
var bodyParser = require('body-parser')
var urlencodedparser = bodyParser.urlencoded({extended:false})

var {getreq,getabs} = require('./getroutes')
var {sub, postabs} = require('./postroutes')
app.set('view engine','ejs')
app.get('/',getreq);
app.get('/abstract',getabs)
app.post('/abstract_summ',urlencodedparser,postabs)
app.post('/submit',urlencodedparser,sub)


app.listen(process.env.PORT || 9900,()=>{
    console.log('Server on 9900')
})