const db = require('../lib/db')

const getAllExercises = async () => {
    const result = await db.query('SELECT * FROM exercises Order by muscle_group asc');
    return result.rows;
};

const getExerciseById = async(id) => {
    const result = await db.query('SELECT * FROM exercises WHERE id = $1', [id]);

    if (result.rows.length === 0) {
        return null;
    }
    
    return result.rows[0];
};

module.exports = {
    getAllExercises,
    getExerciseById
};