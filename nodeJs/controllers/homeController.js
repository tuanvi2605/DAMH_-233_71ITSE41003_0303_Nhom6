const mysql = require('../config/mysql');

const hello = (req, res) => {
    res.send("hello");
}

const getuser = (req, res) => {
    mysql.execute('SELECT * FROM Users', function (err, result, fields) {
        res.send(result)
    })

}

const sampleWeb = (req, res) => {
    res.render('sample');

}

module.exports = { hello, getuser, sampleWeb }