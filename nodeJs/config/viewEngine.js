const app = require('express')

const ConfigViewEngine = (app) => {
    app.set('views', './src/views');
    app.set('view engine', 'ejs');
}

module.exports = ConfigViewEngine;