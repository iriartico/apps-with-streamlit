-- Create a table for countries
CREATE TABLE IF NOT EXISTS country (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Create a table for roles
CREATE TABLE IF NOT EXISTS role (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Create a table for survey responses
CREATE TABLE IF NOT EXISTS surveyresponse (
    id SERIAL PRIMARY KEY,
    role_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    age INTEGER NOT NULL,
    years_of_experience INTEGER NOT NULL,
    salary FLOAT NOT NULL,
    main_skills TEXT NOT NULL,
    submitted_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),

    FOREIGN KEY (role_id) REFERENCES role (id),
    FOREIGN KEY (country_id) REFERENCES country (id)
);