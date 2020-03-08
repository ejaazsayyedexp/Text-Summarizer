const fs = require('fs')
const spawn = require('child_process').spawn



exports.sub = (req,res)=>{
    var textrec = req.body.textName
    var result;
    var pyprocess = spawn('python', ['./datafolder/newtextsummarizer.py',textrec])
    pyprocess.stdout.on('data',(data)=>{
        result = data.toString()
        res.render('home',{stat:"Successful",textSent:result,actText:textrec})
    })
    pyprocess.stderr.on('data',(data)=>{
        console.log("Error occered:",data.toString())
        res.render('home',{stat:"Successful",textSent:"Sorry, an error was occured. MAybe its us.",actText:textrec})
    })
    


}