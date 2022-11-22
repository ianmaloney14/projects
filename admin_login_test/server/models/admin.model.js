const mongoose = require('mongoose')

const AdminSchema = new mongoose.Schema({
    username: {
        type: String,
        required: [
            true, 
            "username is required!"
        ], 
        minLength: [2, "Title must be at least 2 characters"],
        maxLength: [24, "Title be less than 24 characters"],
    },
    password: {
        type: password,
        required: [
            true,
            "password is required"
        ]
    }
},{timestamps:true})

const Admin = mongoose.model('Admin', AdminSchema)
module.exports = Admin