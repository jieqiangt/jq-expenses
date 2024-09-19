CREATE TABLE IF NOT EXISTS dim_categories (
    id SERIAL,
    discretionary BOOLEAN NOT NULL,
    category VARCHAR(50) UNIQUE NOT NULL,
    user_id SMALLINT NOT NULL,
    created_on TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_on TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY(id),
    CONSTRAINT fk_categories_users FOREIGN KEY(user_id) REFERENCES trs_users(id) ON DELETE CASCADE
);