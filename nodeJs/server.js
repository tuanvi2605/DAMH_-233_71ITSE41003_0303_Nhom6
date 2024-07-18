const express = require('express')
const router = express.Router();
const mysql = require('mysql2');

require('dotenv').config();

const app = express();
const port = process.env.PORT

const webApp = require('./routes/web')
app.use('/webApp', webApp)

const ConfigViewEngine = require('./config/viewEngine')
ConfigViewEngine(app);

app.use(express.static('public'));

const connection = require('./config/mysql')

// connection.query(
//     'SELECT * FROM Users',

//     function (err, results, fields) {
//         console.log(results);
//     });

app.get('/hinhanh', function (req, res) {
    connection.execute("SELECT * FROM Users", function (err, result, fields) { let dulieu; dulieu = result, res.send(dulieu); });
})



