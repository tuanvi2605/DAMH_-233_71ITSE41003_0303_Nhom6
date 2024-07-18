const express = require('express');
const router = express.Router();
const { hello, getuser, sampleWeb } = require('../controllers/homeController')

router.get('/user', getuser)
router.get('/hello', hello)
router.get('/sample', sampleWeb)

module.exports = router;
