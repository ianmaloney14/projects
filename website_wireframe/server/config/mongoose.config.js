const mongoose = require('mongoose')

mongoose.connect('mongodb://localhost/****',{
    useNewUrlParser:true,
    useUnifiedTopology:true
})
.then(() => {
    console.log("Connected to **** Db")
}).catch((err) => {
    console.log(err)
})