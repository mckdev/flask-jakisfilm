DROP TABLE IF EXISTS movie;

CREATE TABLE movie (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  youtube_id TEXT NOT NULL
);
