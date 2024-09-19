CREATE TABLE IF NOT EXISTS trs_users (
    id SERIAL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(100) NOT NULL,
    acct_type VARCHAR(25) NOT NULL,
    email CITEXT NOT NULL,
    pw_hash VARCHAR(50) NOT NULL,
    public_key VARCHAR(255) NOT NULL,
    auth_2fa BOOLEAN NOT NULL,
    created_on TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_on TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY(id)
);