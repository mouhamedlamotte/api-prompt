
-- +migrate Up user emailVerified 5/juil/2024
ALTER TABLE users
    ADD COLUMN IF NOT EXISTS emailVerified BOOLEAN NOT NULL DEFAULT FALSE;