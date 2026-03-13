const express = require('express');
const router = express.Router();

const controller = require('../controllers/artists.controller');

router.get('/', controller.getFrontPage);

router.get('/about', controller.getAboutPage);

router.get('/artist/:id', controller.getArtistDetails);

module.exports = router;