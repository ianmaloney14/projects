const mongoose = require('mongoose')

mongoose.connect('mongodb://localhost/adminLogin',{
    useNewUrlParser:true,
    useUnifiedTopology:true
})
.then(() => {
    console.log("Connected to Admin Login Db")
}).catch((err) => {
    console.log(err)
})