const express = require('express'); 
const router = express.Router(); 
const exerciseController = require('.../controllers/exerciseController'); 

router.get('/', exerciseController.getHomePage); 

router.get('/exercises/:id',exerciseController.getExerciseDetail);

module.exports = router;