CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE zones (id SERIAL PRIMARY KEY, name TEXT, description TEXT);
CREATE TABLE threads (id SERIAL PRIMARY KEY, started_by INTEGER REFERENCES users, subject TEXT, zone_id INTEGER REFERENCES zones, created_at TIMESTAMP);
CREATE TABLE messages (id SERIAL PRIMARY KEY, poster_id INTEGER REFERENCES users, msg TEXT, thread_id INTEGER REFERENCES threads, posted_at TIMESTAMP);
