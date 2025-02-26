CREATE TABLE IF NOT EXISTS video_categories (
    id SERIAL PRIMARY KEY,
    category_id INT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    assignable BOOLEAN NOT NULL
);
