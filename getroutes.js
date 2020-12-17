exports.getreq = (req,res)=>{
    res.render('home',{stat:"False"})
}

exports.getabs = (req,res)=>{
    res.render('abshome',{stat:"False"})
}