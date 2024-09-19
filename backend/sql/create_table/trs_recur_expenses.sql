CREATE TABLE IF NOT EXISTS trs_recur_expenses (
    id SERIAL,
    exp_desc VARCHAR(255) NOT NULL,
    amount REAL NOT NULL,
    recurring_period VARCHAR(1) NOT NULL,
    category_id SMALLINT NOT NULL,
    recurring_start DATE NOT NULL,
    recurring_end DATE NOT NULL,
    user_id SMALLINT NOT NULL,
    is_active BOOLEAN NOT NULL,
    created_on TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_on TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY(id),
    CONSTRAINT fk_expenses_category FOREIGN KEY(category_id) REFERENCES dim_categories(id) ON DELETE SET NULL,
    CONSTRAINT fk_expenses_user FOREIGN KEY(user_id) REFERENCES trs_users(id) ON DELETE CASCADE
);