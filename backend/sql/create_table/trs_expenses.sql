CREATE TABLE IF NOT EXISTS trs_expenses (
    id SERIAL,
    exp_date DATE,
    exp_desc VARCHAR(255) NOT NULL,
    amount REAL NOT NULL,
    exp_month SMALLINT NOT NULL,
    exp_year SMALLINT NOT NULL,
    recurring BOOLEAN NOT NULL,
    recurring_period VARCHAR(1),
    category_id SMALLINT NOT NULL,
    recurring_start DATE,
    user_id SMALLINT NOT NULL,
    created_on TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_on TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY(id),
    CONSTRAINT fk_expenses_category FOREIGN KEY(category_id) REFERENCES dim_categories(id) ON DELETE SET NULL,
    CONSTRAINT fk_expenses_user FOREIGN KEY(user_id) REFERENCES trs_users(id) ON DELETE CASCADE
);