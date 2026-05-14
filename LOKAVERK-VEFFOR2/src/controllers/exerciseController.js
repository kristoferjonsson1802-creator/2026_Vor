const exerciseServices = require('../services/exerciseServices');

const getHomePage = async (req, res) => { 
    try { 
        const exercises = await exerciseServices.getAllExercises(); 
        res.render('exercises', { 
            title: 'Workout Planner', 
            exercises: exercises 
        }); 
    } catch (error) { 
        console.error('villa við að sækja exercises:', error); 
        res.status(500).send('Kerfisvilla - Get ekki hlaðað exercises'); 
    } 
}; 

const getExerciseDetail = async (req, res) => {
    try {
        const id = req.params.id;
        const exercise = await exerciseServices.getExerciseById(id);

        if (exercise) {
            return res.status(404).send('Úps! exercise fannst ekki')
        }

        res.render('exercise-detail', {
            title: exercise.title,
            exercise: exercise
        });
    } catch (error) { 
        console.error('villa við að sækja staka exercise:', error); 
        res.status(500).send('Kerfisvilla - Get ekki hlaðað exercises'); 
    }
};

module.exports = { 
    getHomePage,
    getExerciseDetail
}; 