CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    muscle_group VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    image_url VARCHAR(255) NOT NULL
);

CREATE TABLE progress (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    exercise_id INT REFERENCES exercises(id),
    weight INT NOT NULL,
    reps INT NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE workout_plans (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    name VARCHAR(255) NOT NULL
);

CREATE TABLE plan_exercises (
    id SERIAL PRIMARY KEY,
    plan_id INT REFERENCES workout_plans(id),
    exercise_id INT REFERENCES exercises(id),
    sets INT NOT NULL,
    reps INT NOT NULL
);

INSERT INTO exercises 
(name, muscle_group, description, image_url) 
VALUES 
( 'Barbell bench press', 'Chest', 'Chest pressing exercise', '' ), 
( 'Machine chest press', 'Chest', 'Machine chest exercise', '' ), 
( 'High to low cable flys', 'Chest', 'Lower chest cable fly', '' ), 
( 'Pec deck machine', 'Chest', 'Chest isolation machine', '' ), 
( 'Pull ups', 'Back', 'Bodyweight back exercise', '' ), 
( 'Lat pulldown', 'Back', 'Vertical pulling exercise', '' ), 
( 'Seated cable row', 'Back', 'Cable rowing exercise', '' ), 
( 'T-bar row', 'Back', 'Rowing back exercise', '' ), 
( 'Machine row', 'Back', 'Machine rowing exercise', '' ), 
( 'Deadlift', 'Back', 'Heavy full body lift', '' ), 
( 'Back extensions', 'Back', 'Lower back exercise', '' ), 
( 'Squats', 'Legs', 'Compound leg exercise', '' ), 
( 'Leg press', 'Legs', 'Machine leg press', '' ), 
( 'Leg extension', 'Legs', 'Quad isolation exercise', '' ), 
( 'Leg curl', 'Legs', 'Hamstring isolation exercise', '' ), 
( 'Romanian deadlift', 'Legs', 'Hamstring hip hinge', '' ), 
( 'Seated calf raises', 'Legs', 'Calf isolation exercise', '' ), 
( 'Hip thrusts', 'Legs', 'Glute focused exercise', '' ), 
( 'Overhead press', 'Shoulders', 'Shoulder pressing exercise', '' ), 
( 'Machine Shoulder press', 'Shoulders', 'Machine shoulder press', '' ), 
( 'Lateral raises', 'Shoulders', 'Side shoulder exercise', '' ), 
( 'Rear delt fly', 'Shoulders', 'Rear shoulder exercise', '' ), 
( 'Face pulls', 'Shoulders', 'Rear delt cable exercise', '' ), 
( 'Barbell curl', 'Biceps', 'Bicep curling exercise', '' ), 
( 'Preacher curl', 'Biceps', 'Bicep isolation curl', '' ), 
( 'Hammer curl', 'Biceps', 'Neutral grip curl', '' ), 
( 'Tricep pushdown', 'Triceps', 'Cable tricep exercise', '' ), 
( 'Skull crushers', 'Triceps', 'Tricep extension exercise', '' ), 
( 'Dips', 'Triceps', 'Bodyweight tricep exercise', '' ), 
( 'Cable crunches', 'Core', 'Weighted ab exercise', '' ), 
( 'Ab wheel rollouts', 'Core', 'Core rollout exercise', '' ), 
( 'Incline walking', 'Cardio', 'Incline walking cardio', '' ), 
( 'Stairmaster', 'Cardio', 'Stair climbing cardio', '' );