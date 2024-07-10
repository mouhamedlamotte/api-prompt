
-- +migrate Up user emailVerified 5/juil/2024
ALTER TABLE users
    ADD COLUMN IF NOT EXISTS emailverified BOOLEAN NOT NULL DEFAULT FALSE;

-- +migrate Up create transaction table 5/juil/2024
CREATE TABLE IF NOT EXISTS transactions(
    id SERIAL PRIMARY KEY,
    buyer_info JSON NOT NULL,
    amount INTEGER NOT NULL,
    prompt_id INTEGER,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP,
    CONSTRAINT fk_prompt_id FOREIGN KEY(prompt_id) REFERENCES prompts(prompt_id)
);

CREATE TYPE transaction_state as  ENUM ('pending', 'paid', 'cancelled');

ALTER TABLE transactions
    ADD COLUMN IF NOT exists state transaction_state NOT NULL DEFAULT 'pending';