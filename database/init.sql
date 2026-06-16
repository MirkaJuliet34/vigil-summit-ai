-- database/init.sql

CREATE TABLE IF NOT EXISTS leads
(
    id SERIAL PRIMARY KEY,

    name VARCHAR(255),

    email VARCHAR(255),

    phone VARCHAR(50),

    company VARCHAR(255),

    position VARCHAR(255),

    score INTEGER DEFAULT 0,

    status VARCHAR(50),

    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS enriched_profiles
(
    id SERIAL PRIMARY KEY,

    lead_id INTEGER REFERENCES leads(id),

    industry VARCHAR(255),

    company_size VARCHAR(255),

    seniority VARCHAR(255),

    interests TEXT,

    linkedin_url VARCHAR(500),

    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS interactions
(
    id SERIAL PRIMARY KEY,

    lead_id INTEGER REFERENCES leads(id),

    interaction_type VARCHAR(100),

    content TEXT,

    created_at TIMESTAMP DEFAULT NOW()
);