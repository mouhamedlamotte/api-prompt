CREATE TABLE IF NOT EXISTS users(
            uid SERIAL PRIMARY KEY,
            email VARCHAR(250) UNIQUE NOT NULL,
            password VARCHAR(250) NOT NULL,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            is_superuser BOOL DEFAULT FALSE,
            is_staff BOOL DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT NOW(),
            last_login TIMESTAMP
        );

CREATE TABLE IF NOT EXISTS groups (
                    group_id SERIAL PRIMARY KEY,
                    name VARCHAR(100) UNIQUE NOT NULL,
                    created_by INT,
                    created_at TIMESTAMP DEFAULT NOW(),
                    CONSTRAINT fk_created_by FOREIGN KEY(created_by) REFERENCES users(uid)
    );

CREATE TABLE IF NOT EXISTS group_members(
                gm_id SERIAL PRIMARY KEY,
                uid INT,
                group_id INT,
                CONSTRAINT fk_uid FOREIGN KEY(uid) REFERENCES users(uid),
                CONSTRAINT fk_group_id FOREIGN KEY(group_id) REFERENCES groups(group_id)
            );

DO $$ BEGIN
    CREATE TYPE state_type AS ENUM (
    'pending', 
    'active',  
    'review',  
    'reminder', 
    'to_delete' 
    );
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;



CREATE TABLE IF NOT EXISTS prompts(
            prompt_id SERIAL PRIMARY KEY,
            title VARCHAR(250) NOT NULL,
            text VARCHAR(250) NOT NULL,
            tags VARCHAR(300),
            price integer DEFAULT 1000,
            state state_type DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT NOW(),
            created_by INT,
            constraint fk_created_by foreign key(created_by) references users(uid)
        );


CREATE TABLE IF NOT EXISTS votes(
                vote_id SERIAL PRIMARY KEY,
                uid INT,
                prompt_id INT,
                value integer DEFAULT 1,
                CONSTRAINT fk_uid FOREIGN KEY(uid) REFERENCES users(uid),
                CONSTRAINT fk_prompt_id FOREIGN KEY(prompt_id) REFERENCES prompts(prompt_id)
           );


CREATE TABLE IF NOT EXISTS notes(
    note_id SERIAL PRIMARY KEY,
    uid INT,
    prompt_id INT,
    value FLOAT NOT NULL,
    CONSTRAINT fk_uid FOREIGN KEY(uid) REFERENCES users(uid),
    CONSTRAINT fk_prompt_id FOREIGN KEY(prompt_id) REFERENCES prompts(prompt_id)
);


