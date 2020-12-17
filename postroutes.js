const spawn = require('child_process').spawn

exports.sub = (req,res)=>{
    var textrec = req.body.textName
    var pyprocess = spawn('python', ['./datafolder/newtextsummarizer.py',textrec])
    pyprocess.stdout.on('data',(data)=>{
        var result = data.toString()
        //console.log(result)
        res.render('home',{stat:"Successful",textSent:result,actText:textrec})
    })
    pyprocess.stderr.on('data',(data)=>{
        console.log("Error occered:",data.toString())
        res.render('home',{stat:"Successful",textSent:"Sorry, an error was occured. MAybe its us.",actText:textrec})
    })
}
exports.postabs = (req,res)=>{
    var textrec = req.body.textName
    var pyprocess = spawn('python', ['./datafolder/abstextsummarizer.py',textrec])
    pyprocess.stdout.on('data',(data)=>{
        var result = data.toString()
        //console.log(result)
        res.render('abshome',{stat:"Successful",textSent:result,actText:textrec})
    })
    pyprocess.stderr.on('data',(data)=>{
        console.log("Error occered:",data.toString())
        res.render('abshome',{stat:"Successful",textSent:"Sorry, an error was occured. MAybe its us.",actText:textrec})
    })
}
