const db = require('../lib/db');

const getAllExercises = async () => {
    const result = await db.query('SELECT * FROM exercises ORDER BY id ASC');
    return result.rows;
};

module.exports = {
    getAllExercises
};