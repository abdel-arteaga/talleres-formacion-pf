CREATE TABLE IF NOT EXISTS workshops (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    date VARCHAR(20) NOT NULL,
    time VARCHAR(20) NOT NULL,
    place VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS registrations (
    id SERIAL PRIMARY KEY,
    student_name VARCHAR(100),
    workshop_id INTEGER REFERENCES workshops(id) ON DELETE CASCADE
);

-- Datos iniciales
INSERT INTO workshops (name, description, date, time, place, category)
VALUES ('Python Workshop', 'Learn Flask and Docker', '2024-12-01', '10:00', 'Lab 1', 'Technology');
