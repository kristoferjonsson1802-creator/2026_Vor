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
( 'Barbell bench press', 'Chest', 'Chest pressing exercise', '/img/barbellBench.webp' ), 
( 'Machine chest press', 'Chest', 'Machine chest exercise', '/img/machineChest.webp' ), 
( 'High to low cable flys', 'Chest', 'Lower chest cable fly', '/img/httChest.webp' ), 
( 'Pec deck machine', 'Chest', 'Chest isolation machine', '/img/pecDeck.webp' ), 
( 'Pull ups', 'Back', 'Bodyweight back exercise', '/img/pullUps.webp' ), 
( 'Lat pulldown', 'Back', 'Vertical pulling exercise', '/img/latPulldown.webp' ), 
( 'Seated cable row', 'Back', 'Cable rowing exercise', '/img/seatedCableRow.webp' ), 
( 'T-bar row', 'Back', 'Rowing back exercise', '/img/tBarRow.webp' ), 
( 'Machine row', 'Back', 'Machine rowing exercise', '/img/machineRow.webp' ), 
( 'Deadlift', 'Back', 'Heavy full body lift', '/img/deadlift.webp' ), 
( 'Back extensions', 'Back', 'Lower back exercise', '/img/backExtension.webp' ), 
( 'Squats', 'Legs', 'Compound leg exercise', '/img/squat.webp' ), 
( 'Leg press', 'Legs', 'Machine leg press', '/img/legPress.webp' ), 
( 'Leg extension', 'Legs', 'Quad isolation exercise', '/img/legExtension.webp' ), 
( 'Leg curl', 'Legs', 'Hamstring isolation exercise', '/img/legCurl.webp' ), 
( 'Romanian deadlift', 'Legs', 'Hamstring hip hinge', '/img/romainianDeadlift.webp' ), 
( 'Seated calf raises', 'Legs', 'Calf isolation exercise', '/img/calfRaises.webp' ), 
( 'Hip thrusts', 'Legs', 'Glute focused exercise', '/img/hipThrust.webp' ), 
( 'Overhead press', 'Shoulders', 'Shoulder pressing exercise', '/img/overheadPress.webp' ), 
( 'Machine Shoulder press', 'Shoulders', 'Machine shoulder press', '/img/shoulderPress.webp' ), 
( 'Lateral raises', 'Shoulders', 'Side shoulder exercise', '/img/lateralRaises.webp' ), 
( 'Rear delt fly', 'Shoulders', 'Rear shoulder exercise', '/img/rearDfly.webp' ), 
( 'Face pulls', 'Shoulders', 'Rear delt cable exercise', '/img/facePulls.webp' ), 
( 'Barbell curl', 'Biceps', 'Bicep curling exercise', '/img/barbellCurl.webp' ), 
( 'Preacher curl', 'Biceps', 'Bicep isolation curl', '/img/preacherCurl.webp' ), 
( 'Hammer curl', 'Biceps', 'Neutral grip curl', '/img/hammerCurl.webp' ), 
( 'Tricep pushdown', 'Triceps', 'Cable tricep exercise', '/img/triPushdown.webp' ), 
( 'Skull crushers', 'Triceps', 'Tricep extension exercise', '/img/skullCrusher.webp' ), 
( 'Dips', 'Triceps', 'Bodyweight tricep exercise', '/img/dips.webp' ), 
( 'Cable crunches', 'Core', 'Weighted ab exercise', '/img/cableCrunch.webp' ), 
( 'Ab wheel rollouts', 'Core', 'Core rollout exercise', '/img/rollout.webp' ), 
( 'Incline walking', 'Cardio', 'Incline walking cardio', '/img/inclineWalk.webp' ), 
( 'Stairmaster', 'Cardio', 'Stair climbing cardio', '/img/stairmaster.jpg' );